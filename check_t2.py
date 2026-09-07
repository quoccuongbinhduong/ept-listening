import json

text = open('listening.html', encoding='utf-8').read()

# Parse CORE
idx = text.find('const CORE = {')
start = idx + len('const CORE = ')
depth = 0
for i, c in enumerate(text[start:]):
    if c == '{': depth += 1
    elif c == '}': depth -= 1
    if depth == 0:
        end = start + i + 1
        break
core = json.loads(text[start:end].rstrip(';'))

qs = core['questions']['2']
scripts = core['scripts']['2']
answers = core['answers']['2']

print('=== TEST 2 PART 3 (Q41-70) ===')
issues = []
for q in range(41, 71):
    qd = qs.get(str(q), {})
    sd = scripts.get(str(q), {})
    ans = answers.get(str(q), '?')
    opts = qd.get('o', [])
    grp = sd.get('group_script', '')
    qtext = qd.get('q', '')
    
    # Check
    if len(opts) != 4:
        issues.append(f'Q{q}: {len(opts)} options (expected 4)')
    if not qtext:
        issues.append(f'Q{q}: no question text')
    if not grp:
        issues.append(f'Q{q}: no group_script')
    
    # Verify correct answer is within options
    ans_idx = ord(ans) - ord('A') if ans in 'ABCD' else -1
    if ans_idx >= len(opts):
        issues.append(f'Q{q}: answer {ans} but only {len(opts)} options')

print('=== TEST 2 PART 4 (Q71-100) ===')
for q in range(71, 101):
    qd = qs.get(str(q), {})
    sd = scripts.get(str(q), {})
    ans = answers.get(str(q), '?')
    opts = qd.get('o', [])
    grp = sd.get('group_script', '')
    qtext = qd.get('q', '')
    
    if len(opts) != 4:
        issues.append(f'Q{q}: {len(opts)} options (expected 4)')
    if not qtext:
        issues.append(f'Q{q}: no question text')
    if not grp:
        issues.append(f'Q{q}: no group_script')

if issues:
    print('ISSUES FOUND:')
    for iss in issues:
        print(' -', iss)
else:
    print('ALL GOOD! Test 2 Part 3+4: No issues found.')

# Sample some answers
print()
print('Sample Q41-43:')
for q in [41, 42, 43]:
    qd = qs.get(str(q), {})
    ans = answers.get(str(q), '?')
    opts = qd.get('o', [])
    print(f'  Q{q} [{ans}]: {qd.get("q", "")[:50]}')
    for i, o in enumerate(opts):
        print(f'    {"ABCD"[i]}) {o}')
