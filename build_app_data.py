import pdfplumber, json, re

# ─── 1. Parse listening answer keys ───────────────────────────────────────────
listening_answers = {}
with pdfplumber.open('TAI LIEU EPT-TDMU Đáp án.pdf') as pdf:
    current_test = None
    in_listening = True
    for page in pdf.pages:
        text = page.extract_text()
        if not text:
            continue
        for line in text.split('\n'):
            if 'A. LISTENING' in line:
                in_listening = True; continue
            if 'B. READING' in line:
                in_listening = False; continue
            m = re.match(r'Practice Test (\d+)', line.strip())
            if m:
                current_test = int(m.group(1))
                if in_listening and current_test not in listening_answers:
                    listening_answers[current_test] = {}
                continue
            if current_test and in_listening:
                for num, ans in re.findall(r'(\d+)\s+([ABCD])', line):
                    n = int(num)
                    if n <= 100:
                        listening_answers[current_test][n] = ans

print('Listening answers parsed:')
for t in sorted(listening_answers):
    print(f'  Test {t}: {len(listening_answers[t])} answers')

# ─── 2. Parse raw scripts text ─────────────────────────────────────────────────
scripts_raw = {}
with pdfplumber.open('TAI LIEU EPT-TDMU SCRIPTS.pdf') as pdf:
    all_text = ''
    for page in pdf.pages:
        t = page.extract_text()
        if t:
            all_text += t + '\n'

    boundaries = {}
    for m in re.finditer(r'Practice Test (\d+)', all_text):
        t = int(m.group(1))
        if t not in boundaries:
            boundaries[t] = m.start()

    bl = sorted(boundaries.items())
    for i, (t, start) in enumerate(bl):
        end = bl[i+1][1] if i+1 < len(bl) else len(all_text)
        scripts_raw[t] = all_text[start:end]

print('Scripts parsed:')
for t in sorted(scripts_raw):
    print(f'  Test {t}: {len(scripts_raw[t])} chars')

# ─── 3. Build EPT structure info (part boundaries) ─────────────────────────────
# EPT Listening: 100 questions
# Part 1: Photos        Q1-10   (4 options, choose 1 correct description of photo)
# Part 2: Q-Response    Q11-40  (3 options)
# Part 3: Conversations Q41-70  (4 options, grouped by conversations)
# Part 4: Talks         Q71-100 (4 options, grouped by talks)

PARTS = {
    1: {"name": "Part 1: Photos", "start": 1,  "end": 10,  "options": ["A","B","C","D"]},
    2: {"name": "Part 2: Question-Response", "start": 11, "end": 40, "options": ["A","B","C"]},
    3: {"name": "Part 3: Conversations", "start": 41, "end": 70, "options": ["A","B","C","D"]},
    4: {"name": "Part 4: Talks", "start": 71, "end": 100, "options": ["A","B","C","D"]},
}

# ─── 4. Save final JSON ─────────────────────────────────────────────────────────
output = {
    "tests": {},
    "parts": PARTS
}

for t in sorted(listening_answers):
    output["tests"][str(t)] = {
        "answers": {str(k): v for k,v in sorted(listening_answers[t].items())},
        "script": scripts_raw.get(t, "")
    }

with open('ept_app_data.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print('\nSaved ept_app_data.json')
print('Sample answers Test 1:', dict(list(listening_answers[1].items())[:10]))
