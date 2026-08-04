"""
Build full EPT app data:
 1. Crop 10 Part-1 photos from LISTENING PRACTICE-1.pdf (pages 2-6, 2 photos/page)
 2. Parse script text per question using coordinate-aware 2-column extraction
 3. Write all data as embedded JSON into index.html
"""

import fitz, pdfplumber, json, re, base64, os
from PIL import Image
from io import BytesIO

DOC_PATH  = 'LISTENING PRACTICE-1.pdf'
SCRIPT_PATH = 'TAI LIEU EPT-TDMU SCRIPTS.pdf'
ANSWER_PATH = 'TAI LIEU EPT-TDMU Đáp án.pdf'
OUT_HTML  = 'index.html'
IMG_DIR   = 'images/part1'

os.makedirs(IMG_DIR, exist_ok=True)

# ══════════════════════════════════════════════════════════
# 1. EXTRACT PART-1 PHOTOS (pages 2-6, each page has 2 photos)
# ══════════════════════════════════════════════════════════
print("=== Extracting Part 1 photos ===")

doc = fitz.open(DOC_PATH)
photos_b64 = {}   # {q_num: 'data:image/jpeg;base64,...'}

# Pages 2-6 of PDF (index 1-5), each has 2 photos
# Layout: photo 1 in top half, photo 2 in bottom half
# Page size: 1224x1584 (at 2x scale)

PHOTO_PAGES = {
    2: (1, 2),
    3: (3, 4),
    4: (5, 6),
    5: (7, 8),
    6: (9, 10),
}

for page_num, (q1, q2) in PHOTO_PAGES.items():
    page = doc[page_num - 1]  # 0-indexed
    
    # Render at 2x
    mat = fitz.Matrix(2.0, 2.0)
    pix = page.get_pixmap(matrix=mat, alpha=False)
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    
    W, H = img.width, img.height
    
    # Each page: top photo occupies rows ~30px to ~H/2-30, bottom ~H/2 to H-30
    # Determine split by analyzing pixel brightness (find the white gap)
    # Simple approach: top half for q1, bottom half for q2
    margin_top    = int(H * 0.02)
    margin_bottom = int(H * 0.02)
    mid = H // 2
    
    # Add small padding around images
    pad = 15
    
    top_img = img.crop((pad, margin_top, W - pad, mid - pad))
    bot_img = img.crop((pad, mid + pad, W - pad, H - margin_bottom))
    
    for qnum, sub_img in [(q1, top_img), (q2, bot_img)]:
        # Save as JPEG base64
        buf = BytesIO()
        sub_img.save(buf, format='JPEG', quality=80)
        b64 = base64.b64encode(buf.getvalue()).decode()
        photos_b64[qnum] = f"data:image/jpeg;base64,{b64}"
        
        # Also save as file for debugging
        sub_img.save(f"{IMG_DIR}/q{qnum}.jpg", quality=80)
        print(f"  Q{qnum}: {sub_img.size} -> {len(b64)//1024}KB")

print(f"Extracted {len(photos_b64)} photos")

# ══════════════════════════════════════════════════════════
# 2. PARSE SCRIPTS - 2 column aware using pdfplumber words
# ══════════════════════════════════════════════════════════
print("\n=== Parsing scripts (2-column layout) ===")

def reorder_2col(words, page_width):
    """Reorder words from 2-column PDF layout into reading order."""
    mid = page_width / 2
    left_words  = [w for w in words if w['x0'] < mid]
    right_words = [w for w in words if w['x0'] >= mid]
    
    def sort_key(w): return (round(w['top'] / 12) * 12, w['x0'])
    left_words  = sorted(left_words,  key=sort_key)
    right_words = sorted(right_words, key=sort_key)
    
    return left_words + right_words

def words_to_lines(words):
    """Group words by approximate line (within 6px vertical)."""
    if not words: return []
    lines = []
    cur_line = [words[0]]
    for w in words[1:]:
        if abs(w['top'] - cur_line[0]['top']) < 8:
            cur_line.append(w)
        else:
            lines.append(' '.join(x['text'] for x in sorted(cur_line, key=lambda x: x['x0'])))
            cur_line = [w]
    lines.append(' '.join(x['text'] for x in sorted(cur_line, key=lambda x: x['x0'])))
    return lines

# Test page ranges in scripts PDF:
# Test 1: pages 2-7 (index 1-6)
# Test 2: pages 8-14 (index 7-13)
# etc.

TEST_PAGE_RANGES = {
    1: (1, 7),   # 0-indexed
    2: (7, 14),
    3: (14, 21),
    4: (21, 28),
    5: (28, 35),
}

scripts_by_test = {}

with pdfplumber.open(SCRIPT_PATH) as pdf:
    total_pages = len(pdf.pages)
    print(f"Script PDF: {total_pages} pages")
    
    for test_num, (start_p, end_p) in TEST_PAGE_RANGES.items():
        all_lines = []
        for pi in range(start_p, min(end_p, total_pages)):
            page = pdf.pages[pi]
            words = page.extract_words()
            if not words:
                continue
            ordered = reorder_2col(words, page.width)
            lines   = words_to_lines(ordered)
            all_lines.extend(lines)
        
        scripts_by_test[test_num] = '\n'.join(all_lines)
        print(f"  Test {test_num}: {len(all_lines)} lines")

# ══════════════════════════════════════════════════════════
# 3. PARSE SCRIPTS INTO STRUCTURED QUESTIONS
# ══════════════════════════════════════════════════════════
print("\n=== Structuring script questions ===")

OPTION_PAT = re.compile(r'^\(([ABCD])\)\s*(.*)')
QNUM_PAT   = re.compile(r'^(\d{1,3})\.\s*(.*)')
GROUP_PAT  = re.compile(r'Questions?\s+(\d+)[\s\-]+(?:through|and|to|-)*[\s\-]*(\d+)\s+refer', re.IGNORECASE)
PART_PAT   = re.compile(r'PART\s+(\d+)', re.IGNORECASE)

def parse_questions(lines):
    questions = {}   # {qnum: {text, options, group_script}}
    current_q   = None
    current_group_script = []
    in_group_script = False
    group_qs = []
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Part header – skip
        if PART_PAT.match(line):
            i += 1
            continue
        
        # Group reference line e.g. "Questions 41 through 43 refer to..."
        gm = GROUP_PAT.match(line)
        if gm:
            # Save current group script to all questions in group_qs
            if group_qs and current_group_script:
                for q in group_qs:
                    if q in questions:
                        questions[q]['group_script'] = '\n'.join(current_group_script)
            group_qs = list(range(int(gm.group(1)), int(gm.group(2)) + 1))
            current_group_script = [line]
            in_group_script = True
            i += 1
            continue
        
        # Numbered question
        qm = QNUM_PAT.match(line)
        if qm:
            qnum = int(qm.group(1))
            if 1 <= qnum <= 100:
                current_q = qnum
                if current_q not in questions:
                    questions[current_q] = {'text': qm.group(2).strip(), 'options': {}}
                else:
                    questions[current_q]['text'] = qm.group(2).strip()
                in_group_script = False
                i += 1
                continue
        
        # Option line
        om = OPTION_PAT.match(line)
        if om and current_q is not None:
            letter = om.group(1)
            text   = om.group(2).strip()
            # Accumulate multi-line options
            j = i + 1
            while j < len(lines):
                nxt = lines[j].strip()
                if OPTION_PAT.match(nxt) or QNUM_PAT.match(nxt) or GROUP_PAT.match(nxt):
                    break
                if nxt and not PART_PAT.match(nxt):
                    text += ' ' + nxt
                j += 1
            questions[current_q]['options'][letter] = text.strip()
            i = j
            continue
        
        # Group script content (narration/conversation lines)
        if in_group_script:
            if line:
                current_group_script.append(line)
        
        i += 1
    
    # Save last group
    if group_qs and current_group_script:
        for q in group_qs:
            if q in questions:
                questions[q]['group_script'] = '\n'.join(current_group_script)
    
    return questions

structured_scripts = {}
for test_num, text in scripts_by_test.items():
    lines = text.split('\n')
    qs = parse_questions(lines)
    structured_scripts[test_num] = qs
    
    # Report coverage
    covered = len(qs)
    has_opts = sum(1 for q in qs.values() if q.get('options'))
    has_grp  = sum(1 for q in qs.values() if q.get('group_script'))
    print(f"  Test {test_num}: {covered} questions, {has_opts} with options, {has_grp} with group scripts")
    
    # Show samples
    for qn in sorted(qs.keys())[:3]:
        q = qs[qn]
        print(f"    Q{qn}: {q['text'][:60]}")
        for k,v in q['options'].items():
            print(f"      ({k}) {v[:50]}")

# ══════════════════════════════════════════════════════════
# 4. PARSE ANSWERS
# ══════════════════════════════════════════════════════════
print("\n=== Parsing answers ===")

answers = {}
with pdfplumber.open(ANSWER_PATH) as pdf:
    current_test = None
    in_listening = True
    for page in pdf.pages:
        text = page.extract_text()
        if not text:
            continue
        for line in text.split('\n'):
            if 'A. LISTENING' in line:
                in_listening = True; continue
            if 'B. READING'   in line:
                in_listening = False; continue
            m = re.match(r'Practice Test (\d+)', line.strip())
            if m:
                current_test = int(m.group(1))
                if in_listening and current_test not in answers:
                    answers[current_test] = {}
                continue
            if current_test and in_listening:
                for num, ans in re.findall(r'(\d+)\s+([ABCD])', line):
                    n = int(num)
                    if n <= 100:
                        answers[current_test][n] = ans

for t in sorted(answers):
    print(f"  Test {t}: {len(answers[t])} answers")

# ══════════════════════════════════════════════════════════
# 5. SERIALIZE TO JSON
# ══════════════════════════════════════════════════════════
print("\n=== Serializing data ===")

# Convert structured_scripts to JSON-serializable
scripts_json = {}
for t, qs in structured_scripts.items():
    scripts_json[str(t)] = {}
    for qn, q in qs.items():
        scripts_json[str(t)][str(qn)] = {
            'text': q.get('text', ''),
            'options': q.get('options', {}),
            'group_script': q.get('group_script', ''),
        }

answers_json = {}
for t, ans_dict in answers.items():
    answers_json[str(t)] = {str(k): v for k, v in ans_dict.items()}

photos_json = {str(k): v for k, v in photos_b64.items()}

# Print total size estimate
total_kb = sum(len(v)//1024 for v in photos_b64.values())
print(f"Photos total: ~{total_kb} KB (base64)")

data_payload = {
    'answers': answers_json,
    'scripts': scripts_json,
    'photos':  photos_json,
}

with open('app_data.json', 'w', encoding='utf-8') as f:
    json.dump(data_payload, f, ensure_ascii=False)

size_kb = os.path.getsize('app_data.json') // 1024
print(f"Saved app_data.json: {size_kb} KB")
print("Done! Ready to build HTML.")
