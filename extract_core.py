import json

with open('listening.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract CORE JSON
start = content.index('const CORE = ') + len('const CORE = ')
# Find matching brace
depth = 0
end = start
for i in range(start, len(content)):
    if content[i] == '{':
        depth += 1
    elif content[i] == '}':
        depth -= 1
        if depth == 0:
            end = i + 1
            break

core_json = content[start:end]
core = json.loads(core_json)

# Save answers, scripts, questions for the AI
data = {
    'answers': core['answers'],
    'scripts': core['scripts'],
    'questions': core.get('questions', {})
}

with open('core_for_expl.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, separators=(',',':'))

print('Saved core_for_expl.json')
print('Tests in answers:', list(data['answers'].keys()))
print('Tests in scripts:', list(data['scripts'].keys()))
print('Tests in questions:', list(data['questions'].keys()))

for t in data['answers']:
    ans_count = len(data['answers'][t])
    scr_count = len(data['scripts'].get(t, {}))
    q_count = len(data['questions'].get(t, {}))
    print(f'Test {t}: answers={ans_count}, scripts={scr_count}, questions={q_count}')
