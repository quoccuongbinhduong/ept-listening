import json, re, sys

print("Loading explanations.json...")
with open('explanations.json', 'r', encoding='utf-8') as f:
    explanations = json.load(f)

print("Loading listening.html...")
with open('listening.html', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"HTML size: {len(content):,} chars")

CORE_START_MARKER = 'const CORE = '
core_start_pos = content.index(CORE_START_MARKER) + len(CORE_START_MARKER)

depth = 0
core_end_pos = core_start_pos
for i in range(core_start_pos, len(content)):
    if content[i] == '{':
        depth += 1
    elif content[i] == '}':
        depth -= 1
        if depth == 0:
            core_end_pos = i + 1
            break

print(f"CORE JSON found: chars {core_start_pos}–{core_end_pos}")
core_json_raw = content[core_start_pos:core_end_pos]
core = json.loads(core_json_raw)

print("Injecting explanations...")
q_injected = 0
for test_str, test_expls in explanations.items():
    if test_str not in core.get('questions', {}):
        core.setdefault('questions', {})[test_str] = {}
    for q_str, expl_text in test_expls.items():
        qn = int(q_str)
        if qn >= 41:
            if q_str in core['questions'].get(test_str, {}):
                core['questions'][test_str][q_str]['e'] = expl_text
                q_injected += 1
            else:
                core['questions'].setdefault(test_str, {})[q_str] = {'e': expl_text}
                q_injected += 1

s_injected = 0
for test_str, test_expls in explanations.items():
    for q_str, expl_text in test_expls.items():
        qn = int(q_str)
        if qn <= 40:
            if test_str in core.get('scripts', {}) and q_str in core['scripts'][test_str]:
                core['scripts'][test_str][q_str]['e'] = expl_text
                s_injected += 1

print(f"Injected into questions: {q_injected}")
print(f"Injected into scripts:   {s_injected}")

print("Serializing updated CORE...")
new_core_json = json.dumps(core, ensure_ascii=False, separators=(',', ':'))
new_core_json = new_core_json.replace('</', r'<\/')
new_content = content[:core_start_pos] + new_core_json + content[core_end_pos:]

# Patch the JS EXPLANATION rendering block
js_start = new_content.find("const explBox = $('qexpl');")
js_end = new_content.find("  $('bprev').disabled = (qn === 1);", js_start)

if js_start != -1 and js_end != -1:
    NEW_EXPL_JS = """const explBox = $('qexpl');
  const explContent = $('expl-content');
  if (explBox && explContent) {
      if (isDone) {
          explBox.classList.remove('hidden');
          const explNote = (qd && qd.e) ? qd.e : (sd && sd.e ? sd.e : '');
          if (explNote) {
              const fmtNote = explNote.replace(/\\n/g, '<br>');
              explContent.innerHTML = `<div class="expl-sec expl-note"><div class="expl-note-body">${fmtNote}</div></div>`;
          } else {
              explContent.innerHTML = '';
          }
      } else {
          explBox.classList.add('hidden');
      }
  }
"""
    new_content = new_content[:js_start] + NEW_EXPL_JS + new_content[js_end:]
    print("✅ JS EXPLANATION block patched successfully")
else:
    print("❌ Could not find JS block to patch! Aborting.")
    sys.exit(1)


# Inject CSS
if ".expl-note-body{" not in new_content:
    css_block = """
.expl-sec{background:rgba(255,255,255,.04);border-radius:8px;padding:10px 12px;margin-bottom:8px;}
.expl-sec-lbl{font-size:11px;font-weight:700;color:var(--acc2);text-transform:uppercase;letter-spacing:.8px;margin-bottom:6px;}
.expl-q{font-size:12.5px;color:var(--txt);margin-bottom:5px;padding:4px 8px;background:rgba(108,99,255,.1);border-radius:5px;}
.expl-opt{font-size:12.5px;color:var(--mut);padding:2px 0;}
.expl-opt-ok{font-size:12.5px;color:var(--grn);font-weight:600;padding:2px 0;}
.expl-script{font-size:12px;color:var(--mut);white-space:pre-wrap;line-height:1.6;max-height:160px;overflow-y:auto;padding:4px 2px;}
.expl-ans{font-size:13px;font-weight:700;color:var(--grn);padding:6px 0 4px;}
.expl-note{border-left:3px solid var(--acc2);background:rgba(167,139,250,.08);}
.expl-note-body{font-size:13.5px;color:var(--txt);line-height:1.75;}
"""
    style_close = new_content.rfind('</style>')
    if style_close != -1:
        new_content = new_content[:style_close] + css_block + new_content[style_close:]
        print("✅ CSS injected before </style>")

with open('listening.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print(f"✅ Done! File size: {len(new_content):,} chars")
