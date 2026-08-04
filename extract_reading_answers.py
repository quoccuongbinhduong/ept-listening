import fitz
import json
import re

doc = fitz.open('TAI LIEU EPT-TDMU Đáp án.pdf')
text = ''
for p in doc:
    text += p.get_text() + '\n'

idx = text.find('Practice Test 1')
if idx == -1:
    print("Could not find Practice Test 1")
    exit(1)

text = text[idx:]

# The text contains "Practice Test X" followed by lines like "101 A 111 A ..."
tests = {}
current_test = 0

lines = text.split('\n')
for line in lines:
    m_test = re.match(r'Practice Test (\d)', line.strip())
    if m_test:
        current_test = int(m_test.group(1))
        tests[current_test] = {}
        continue
    
    if current_test > 0:
        # Find pairs of (QuestionNumber, Answer)
        matches = re.findall(r'(\d{3})\s+([A-D])', line)
        for q, a in matches:
            tests[current_test][q] = a

with open('reading_answers.json', 'w', encoding='utf-8') as f:
    json.dump(tests, f, indent=2)

print("Extracted answers for tests:", list(tests.keys()))
for t in tests:
    print(f"Test {t}: {len(tests[t])} answers")
