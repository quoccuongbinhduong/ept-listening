"""Embed core.json (108KB) directly into index.html — safe size, no fetch issues."""
import json, os, re

with open('core.json', encoding='utf-8') as f:
    core_str = f.read()

# Make sure no </script> tag in data (would break HTML)
core_str = core_str.replace('</script>', r'<\/script>')

html = open('index_template.html', encoding='utf-8').read()
html = html.replace('/*__CORE_DATA__*/', core_str)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"index.html: {os.path.getsize('index.html')//1024} KB")

# Verify no syntax issue
import subprocess
result = subprocess.run(['python', '-c', 
    'import json; d=json.loads(open("core.json",encoding="utf-8").read()); print("OK:", len(d["answers"]), "tests,", sum(len(v) for v in d["answers"].values()), "answers")'],
    capture_output=True, text=True)
print(result.stdout.strip())
