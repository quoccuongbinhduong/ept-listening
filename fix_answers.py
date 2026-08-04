import pdfplumber, json, re

answers = {}
current_test = None

with pdfplumber.open('TAI LIEU EPT-TDMU Đáp án.pdf') as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if not text: continue
        
        for line in text.split('\n'):
            line = line.strip()
            # Match test header like "Practice Test 1" or "Practice Test  Practice Test 1"
            m_test = re.search(r'Practice Test\s+(\d+)', line)
            if m_test:
                t_num = m_test.group(1)
                if t_num not in answers:
                    answers[t_num] = {}
                current_test = t_num
                # some lines have both test header and answers, but usually they are separate
            
            if current_test:
                # Find all pairs of (number) (letter)
                # Like "1 B 11 C 21 B" or "101 A 111 A"
                # Some lines might have extra spaces
                pairs = re.findall(r'\b(\d{1,3})\s+([A-D])\b', line)
                for qnum, ans in pairs:
                    answers[current_test][qnum] = ans

# Wait, the PDF contains Reading answers too (101-200)!
# We only want 1-100 for listening, but extracting all is fine.
# Let's filter to 1-100 to be safe for EPT Listening.

listening_answers = {}
for t, ans_dict in answers.items():
    listening_answers[t] = {}
    for q, a in ans_dict.items():
        if 1 <= int(q) <= 100:
            listening_answers[t][q] = a

# Save it
with open('answers.json', 'w', encoding='utf-8') as f:
    json.dump(listening_answers, f, indent=2)

print("Parsed tests:", list(listening_answers.keys()))
for t in listening_answers:
    print(f"Test {t} has {len(listening_answers[t])} answers")
