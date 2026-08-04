import json
import re

html_path = r"D:\EPT\ept-deploy\index.html"
core_path = r"D:\EPT\ept-deploy\core.json"

with open(core_path, 'r', encoding='utf-8') as f:
    core_content = f.read()

with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Replace the const CORE = {...} line
# It spans multiple lines or one line. Let's find it using regex.
new_html = re.sub(r'const CORE = \{.*?\};\n', f'const CORE = {core_content};\n', html_content, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Updated index.html with new CORE data.")
