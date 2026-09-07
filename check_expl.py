import json

text = open('listening.html', encoding='utf-8').read()

# Parse EXPLANATIONS
idx = text.find('const EXPLANATIONS = {')
start = idx + len('const EXPLANATIONS = ')
depth = 0
for i, c in enumerate(text[start:]):
    if c == '{': depth += 1
    elif c == '}': depth -= 1
    if depth == 0:
        end = start + i + 1
        break

expl = json.loads(text[start:end])

# Check Test 2 Part 3 & 4
t2_expl = expl.get('2', {})

print('=== TEST 2 EXPLANATIONS ===')
missing = [q for q in range(41, 101) if str(q) not in t2_expl]
if missing:
    print(f'MISSING explanations for Q: {missing}')
else:
    print(f'All Q41-100 have explanations. OK!')

print()
print('Sample Q41-43 explanations:')
for q in [41, 42, 43]:
    exp = t2_expl.get(str(q), '(MISSING)')
    print(f'Q{q}: {exp[:100]}...')
    print()

print('Sample Q71-73 explanations (Part 4):')
for q in [71, 72, 73]:
    exp = t2_expl.get(str(q), '(MISSING)')
    print(f'Q{q}: {exp[:100]}...')
    print()
