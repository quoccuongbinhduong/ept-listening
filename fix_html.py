import json

html_path = r"D:\EPT\ept-deploy\index.html"
core_path = r"D:\EPT\ept-deploy\core.json"

with open(core_path, 'r', encoding='utf-8') as f:
    core_content = f.read()

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# We need to find where const CORE = ... starts and ends.
# Since the current index.html has broken newlines, we can't easily rely on just "const CORE".
# Let's find "// ═══════════════════ INLINE DATA (core only) ═══════════════════"
start_marker = "// ═══════════════════ INLINE DATA (core only) ═══════════════════"
start_idx = html.find(start_marker)
if start_idx == -1:
    print("Could not find INLINE DATA marker")
    exit(1)

# The end of the inline data is where the next section starts, e.g., "// Photos loaded lazily"
end_marker = "// Photos loaded lazily"
end_idx = html.find(end_marker)
if end_idx == -1:
    print("Could not find end marker")
    exit(1)

new_block = f"""{start_marker}
const CORE = {core_content};
const ANSWERS = CORE.answers;
const SCRIPTS = CORE.scripts;
const QUESTIONS = CORE.questions || {{}};

"""

new_html = html[:start_idx] + new_block + html[end_idx:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Fixed index.html successfully.")
