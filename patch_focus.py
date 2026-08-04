import re

with open('index.html', encoding='utf-8') as f:
    html = f.read()

# 1. ADD CSS
css = """
/* FOCUS MODE */
.focus-toggle { display:inline-flex; align-items:center; cursor:pointer; gap:6px; background:var(--surf2); border:1px solid var(--bdr); padding:5px 10px; border-radius:8px; margin-right:8px; }
.focus-toggle input { display:none; }
.focus-slider { width:26px; height:14px; background:var(--mut); border-radius:7px; position:relative; transition:0.2s; }
.focus-slider::before { content:''; position:absolute; left:2px; top:2px; width:10px; height:10px; background:#fff; border-radius:50%; transition:0.2s; }
.focus-toggle input:checked + .focus-slider { background:var(--acc); }
.focus-toggle input:checked + .focus-slider::before { transform:translateX(12px); }
.focus-lbl { font-size:11px; font-weight:700; color:var(--txt); user-select:none; }

body.focus-mode .gscript { filter: blur(5px); opacity: 0.5; transition: all 0.3s; }
body.focus-mode .gscript:hover { filter: blur(0); opacity: 1; }
body.focus-mode .qpanel[data-part="2"] .qtxt { filter: blur(5px); opacity: 0.3; transition: all 0.3s; }
body.focus-mode .qpanel[data-part="2"] .qtxt:hover { filter: blur(0); opacity: 1; }
body.focus-mode .qpanel[data-part="2"] .obtn div:nth-child(2) { filter: blur(5px); opacity: 0.3; transition: all 0.3s; }
body.focus-mode .qpanel[data-part="2"] .obtn:hover div:nth-child(2) { filter: blur(0); opacity: 1; }

::-webkit-scrollbar{width:4px;}"""

if "/* FOCUS MODE */" not in html:
    html = html.replace("::-webkit-scrollbar{width:4px;}", css)

# 2. ADD TOGGLE HTML
toggle_html = """
    <div style="display:flex; align-items:center;">
      <label class="focus-toggle" title="Ẩn Script và Đáp án Part 2 để luyện phản xạ">
        <input type="checkbox" id="focusToggle" onchange="toggleFocusMode()">
        <span class="focus-slider"></span>
        <span class="focus-lbl">Luyện Nghe</span>
      </label>
      <div class="sbadge" id="sbadge">Đã làm: <span id="sdone">0</span>/100</div>
    </div>
"""
if "focusToggle" not in html:
    html = html.replace('<div class="sbadge" id="sbadge">Đã làm: <span id="sdone">0</span>/100</div>', toggle_html)

# 3. SET DATA-PART ON QPANEL IN RENDERQ
render_qpanel = "$('qpartl').textContent = part.name;"
render_qpanel_new = "$('qpartl').textContent = part.name;\n  $('qpanel').setAttribute('data-part', part.id);"
if "setAttribute('data-part'" not in html:
    html = html.replace(render_qpanel, render_qpanel_new)

# 4. ADD JS LOGIC
js_logic = """
// ═══════════════════ FOCUS MODE ═══════════════════════════════
function toggleFocusMode() {
  const isFocus = $('focusToggle').checked;
  if (isFocus) {
    document.body.classList.add('focus-mode');
    localStorage.setItem('ept_focus_mode', '1');
  } else {
    document.body.classList.remove('focus-mode');
    localStorage.setItem('ept_focus_mode', '0');
  }
}

// Restore focus mode state
window.addEventListener('DOMContentLoaded', () => {
  if (localStorage.getItem('ept_focus_mode') === '1') {
    const el = $('focusToggle');
    if (el) { el.checked = true; toggleFocusMode(); }
  }
});
"""

if "toggleFocusMode()" not in html:
    # insert before function loadT(id)
    html = html.replace("function loadT(id)", js_logic + "\nfunction loadT(id)")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html patched with Focus Mode successfully.")
