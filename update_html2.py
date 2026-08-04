import re

html_path = r"D:\EPT\ept-deploy\index.html"
core_path = r"D:\EPT\ept-deploy\core.json"

with open(core_path, 'r', encoding='utf-8') as f:
    core_content = f.read()

with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

start_marker = r"// ═══════════════════ INLINE DATA \(core only\) ═══════════════════"
end_marker = r"const ANSWERS = CORE\.answers;"

pattern = re.compile(f'({start_marker}).*?({end_marker})', re.DOTALL)

# Also, update const QUESTIONS = CORE.questions || {};
replacement = f"\\1\nconst CORE = {core_content};\nconst ANSWERS = CORE.answers;\nconst SCRIPTS = CORE.scripts;\nconst QUESTIONS = CORE.questions || {{}};"

# Also we need to remove the old const SCRIPTS = CORE.scripts; since we are adding it above.
# Actually let's just replace from start_marker up to the function getPart(q) or whatever is next.

# Let's just find the exact block to replace manually:
new_html = html_content

# Find the block
start_idx = new_html.find("// ═══════════════════ INLINE DATA (core only) ═══════════════════")
end_idx = new_html.find("function getPart(q)")

if start_idx != -1 and end_idx != -1:
    block = f"""// ═══════════════════ INLINE DATA (core only) ═══════════════════
const CORE = {core_content};
const ANSWERS = CORE.answers;
const SCRIPTS = CORE.scripts;
const QUESTIONS = CORE.questions || {{}};

"""
    new_html = new_html[:start_idx] + block + new_html[end_idx:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Replaced CORE block successfully.")
