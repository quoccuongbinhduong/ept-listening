"""Validate index.html JS can be parsed and CORE data is valid."""
import json, re

with open('index.html', encoding='utf-8') as f:
    html = f.read()

# Extract the CORE = ... assignment
m = re.search(r'const CORE = (\{.*?\});', html, re.DOTALL)
if not m:
    print("ERROR: Could not find 'const CORE = {...}' in index.html")
    exit(1)

core_str = m.group(1)
print(f"CORE string length: {len(core_str)} chars")

try:
    core = json.loads(core_str)
    print("JSON parse: OK")
    print(f"  answers: {len(core['answers'])} tests")
    print(f"  scripts: {len(core['scripts'])} tests")
    for t in ['1','2','3','4','5']:
        n_ans = len(core['answers'].get(t, {}))
        n_scr = len(core['scripts'].get(t, {}))
        print(f"  Test {t}: {n_ans} answers, {n_scr} script entries")
except json.JSONDecodeError as e:
    print(f"JSON parse ERROR at pos {e.pos}: {e.msg}")
    snippet = core_str[max(0,e.pos-50):e.pos+50]
    print(f"  Context: ...{repr(snippet)}...")

# Check for dangerous patterns
dangerous = ['</script>', '`', '${']
for pat in dangerous:
    # Skip the escaped version
    if pat == '</script>':
        if pat.replace('/', r'\/') not in core_str and pat in core_str:
            print(f"WARNING: Found unescaped '{pat}' in CORE data!")
        else:
            print(f"OK: No unescaped '{pat}' in CORE")
    elif pat in core_str:
        idx = core_str.index(pat)
        print(f"WARNING: Found '{pat}' at pos {idx}: ...{repr(core_str[max(0,idx-20):idx+30])}...")
    else:
        print(f"OK: No '{pat}' in CORE")
