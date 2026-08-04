import re

with open('index.html', encoding='utf-8') as f:
    html = f.read()

# 1. Remove loadPhotos();
html = html.replace('if (t === 1) loadPhotos();', '')

# 2. Append toggleFocusMode before </script>
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
</script>
"""

# Avoid double injection if I run it multiple times
if "function toggleFocusMode()" not in html:
    # First, let's clean up any broken tags from my powershell failure
    html = html.replace('</script>', js_logic)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixed index.html successfully.")
