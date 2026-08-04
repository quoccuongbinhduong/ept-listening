"""
Build index.html hoàn chỉnh với:
- Ảnh Part 1 cho cả 5 bài Test (từ Listening_0001.pdf)
- Câu hỏi + đáp án Part 3&4 cho cả 5 bài
- Scripts (hội thoại) cho tất cả Parts
- Đáp án tất cả
"""
import json, fitz, base64, re
from PIL import Image
from io import BytesIO

print("=== BUILD INDEX.HTML ===")

# ── 1. Load answer keys ──────────────────────────────────────
print("1. Loading answers...")
answers = json.load(open('answers.json', encoding='utf-8'))
print(f"   Tests: {list(answers.keys())}")

# ── 2. Load scripts ──────────────────────────────────────────
print("2. Loading scripts...")
scripts = json.load(open('scripts_structured.json', encoding='utf-8'))
print(f"   Tests with scripts: {list(scripts.keys())}")

# ── 3. Load questions (Part 3 & 4) ──────────────────────────
print("3. Loading questions...")
questions = {}
for fname, t_list in [
    ('questions_1.json', ['1']),
    ('questions_2.json', ['2']),
    ('questions_3.json', ['3']),
    ('questions_4.json', ['4']),
    ('questions_5.json', ['5']),
]:
    try:
        data = json.load(open(fname, encoding='utf-8'))
        for t in data:
            if t not in questions:
                questions[t] = data[t]
            else:
                questions[t].update(data[t])
    except FileNotFoundError:
        print(f"   WARNING: {fname} not found, skipping")

for t in sorted(questions.keys()):
    q_nums = sorted(int(k) for k in questions[t].keys())
    print(f"   Test {t}: questions {min(q_nums)}-{max(q_nums)} ({len(q_nums)} total)")

# ── 4. Extract photos from Listening_0001.pdf ────────────────
print("4. Extracting photos from Listening_0001.pdf...")
doc = fitz.open('Listening_0001.pdf')
print(f"   Total pages: {len(doc)}")

# PDF structure (12 pages per test):
#   Page offset 0: "PRACTICE TEST N" title
#   Page offset 1: Instructions + sample question (SKIP)
#   Page offsets 2-6: Part 1 photos (2 photos per page = 10 photos)
#   Page offsets 7-11: Parts 2-4 question/script pages

PAGES_PER_TEST = 12
PHOTO_OFFSETS = range(2, 7)  # 5 pages × 2 photos = 10 photos per test

def extract_two_photos(page, q1, q2):
    """Crop top and bottom photos from a page. Each half has: number + photo + whitespace."""
    mat = fitz.Matrix(2.0, 2.0)
    pix = page.get_pixmap(matrix=mat, alpha=False)
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    W, H = img.width, img.height
    pad_x = int(W * 0.04)
    # Crop just the photo area in each half (avoiding question numbers and whitespace)
    crops = {
        str(q1): img.crop((pad_x, int(H*0.04), W-pad_x, int(H*0.48))),
        str(q2): img.crop((pad_x, int(H*0.52), W-pad_x, int(H*0.96))),
    }
    result = {}
    for qn, cropped in crops.items():
        buf = BytesIO()
        cropped.save(buf, format='JPEG', quality=80)
        result[qn] = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    return result

photos_all = {}
for test_num in range(1, 6):
    test_photos = {}
    base_page = (test_num - 1) * PAGES_PER_TEST
    q_counter = 1
    for offset in PHOTO_OFFSETS:
        page_idx = base_page + offset
        if page_idx >= len(doc):
            break
        extracted = extract_two_photos(doc[page_idx], q_counter, q_counter+1)
        test_photos.update(extracted)
        print(f"   Test {test_num}: page {page_idx+1} → Q{q_counter}, Q{q_counter+1}")
        q_counter += 2
    photos_all[str(test_num)] = test_photos
    print(f"   Test {test_num}: {len(test_photos)} photos ✓")

# ── 5. Build payload ─────────────────────────────────────────
print("5. Building payload...")
payload = {
    'answers':   answers,
    'scripts':   scripts,
    'questions': questions,
    'photos':    photos_all,
}
payload_json = json.dumps(payload, ensure_ascii=False, separators=(',', ':'))
print(f"   Payload: {len(payload_json)//1024} KB")

# ── 6. Load index.html and replace CORE block ────────────────
print("6. Updating index.html...")
with open('index.html', encoding='utf-8') as f:
    html = f.read()

# 6a. Find and replace the entire `const CORE = {...};` block
core_start = html.find('const CORE = {')
if core_start == -1:
    print("ERROR: 'const CORE = {' not found in index.html")
    exit(1)

# Walk braces to find matching end
depth = 0
i = core_start + len('const CORE = ')  # points at '{'
while i < len(html):
    if html[i] == '{':
        depth += 1
    elif html[i] == '}':
        depth -= 1
        if depth == 0:
            i += 1  # after '}'
            if i < len(html) and html[i] == ';':
                i += 1  # after ';'
            break
    i += 1
core_end = i

new_core = f'const CORE = {payload_json};'
html = html[:core_start] + new_core + html[core_end:]
print(f"   Replaced CORE block")

# 6b. Fix/add variable declarations after CORE
# Remove old declarations and insert clean ones
old_decls_pattern = re.compile(
    r'\n+const ANSWERS\s*=\s*CORE\.answers;.*?'
    r'(?:\n+const SCRIPTS\s*=\s*CORE\.scripts;.*?)?'
    r'(?:\n+const QUESTIONS\s*=\s*CORE\.questions.*?)?'
    r'(?:\n+const PHOTOS\s*=\s*CORE\.photos.*?)?'
    r'(?:\n+const PARTS\s*=)',
    re.DOTALL
)
new_decls = """

const ANSWERS   = CORE.answers;
const SCRIPTS   = CORE.scripts;
const QUESTIONS = CORE.questions || {};
const PHOTOS    = CORE.photos;

const PARTS ="""

if old_decls_pattern.search(html):
    html = old_decls_pattern.sub(new_decls, html, count=1)
    print("   Replaced variable declarations")
else:
    # Try simpler: just look for ANSWERS declaration
    simple_pattern = re.compile(r'\n+const ANSWERS\s*=\s*CORE\.answers;[^\n]*\n')
    if simple_pattern.search(html):
        html = simple_pattern.sub(
            '\n\nconst ANSWERS   = CORE.answers;\n'
            'const SCRIPTS   = CORE.scripts;\n'
            'const QUESTIONS = CORE.questions || {};\n'
            'const PHOTOS    = CORE.photos;\n',
            html, count=1)
        print("   Updated ANSWERS declaration (added QUESTIONS/PHOTOS)")
    else:
        print("   WARNING: Could not find ANSWERS declaration to update")

# 6c. Fix renderQ: add QUESTIONS lookup before question text
Q_LOOKUP = "const qd = ((QUESTIONS[String(curT)] || {})[String(qn)]) || null;"
if Q_LOOKUP not in html:
    # Find "// Question text" inside renderQ and add qd lookup
    old_qt = "  // Question text\n  const qtxtEl = $('qtxt');\n  if (sd.text && part.id !== 1) {\n    qtxtEl.textContent = sd.text;"
    new_qt = (
        "  // Question text\n"
        f"  {Q_LOOKUP}\n"
        "  const qtxtEl = $('qtxt');\n"
        "  if (qd && qd.q) {\n"
        "    qtxtEl.textContent = qd.q;\n"
        "  } else if (sd.text && part.id !== 1) {\n"
        "    qtxtEl.textContent = sd.text;"
    )
    if old_qt in html:
        html = html.replace(old_qt, new_qt, 1)
        print("   Added QUESTIONS lookup to renderQ")
    else:
        print("   WARNING: Could not find question text block to update")
else:
    print("   QUESTIONS lookup already present")

# 6d. Fix options to use QUESTIONS data
if "letterMap" not in html or "qd.o" not in html:
    old_opts = (
        "  const scriptOpts = sd.options || {};\n"
        "  part.opts.forEach(letter => {\n"
        "    const txt = scriptOpts[letter] || `Đáp án ${letter}`;"
    )
    new_opts = (
        "  const scriptOpts = sd.options || {};\n"
        "  const letterMap = {'A': 0, 'B': 1, 'C': 2, 'D': 3};\n"
        "  part.opts.forEach(letter => {\n"
        "    let txt = `Đáp án ${letter}`;\n"
        "    if (qd && qd.o && qd.o[letterMap[letter]]) {\n"
        "      txt = qd.o[letterMap[letter]];\n"
        "    } else if (scriptOpts[letter]) {\n"
        "      txt = scriptOpts[letter];\n"
        "    }"
    )
    if old_opts in html:
        html = html.replace(old_opts, new_opts, 1)
        print("   Updated options rendering")
    else:
        print("   WARNING: Could not find options block to update")
else:
    print("   Options rendering already updated")

# 6e. Fix photo lookup to use per-test structure
if "testPhotos" not in html:
    for old_p, label in [
        ("  // Photo (Part 1, Test 1 only)\n  const photoWrap = $('qphoto');\n  const photoImg = $('qpimg');\n  if (part.id === 1 && curT === 1 && PHOTOS[String(qn)]) {\n    photoWrap.classList.remove('hidden');\n    photoImg.src = PHOTOS[String(qn)];", "v1"),
        ("  // Photo (Part 1)\n  const photoWrap = $('qphoto');\n  const photoImg = $('qpimg');\n  const pList = PHOTOS[String(curT)] || {};\n  if (part.id === 1 && pList[String(qn)]) {\n    photoWrap.classList.remove('hidden');\n    photoImg.src = pList[String(qn)];", "v2"),
    ]:
        if old_p in html:
            new_p = (
                "  // Photo (Part 1 – all tests)\n"
                "  const photoWrap = $('qphoto');\n"
                "  const photoImg = $('qpimg');\n"
                "  const testPhotos = PHOTOS[String(curT)] || {};\n"
                "  if (part.id === 1 && testPhotos[String(qn)]) {\n"
                "    photoWrap.classList.remove('hidden');\n"
                "    photoImg.src = testPhotos[String(qn)];"
            )
            html = html.replace(old_p, new_p, 1)
            print(f"   Updated photo lookup ({label})")
            break
    else:
        print("   WARNING: Could not find photo block to update")
else:
    print("   Photo lookup already per-test")

# ── 7. Write output ──────────────────────────────────────────
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\n✅ index.html written — {len(html)//1024} KB")
print("  ✅ Part 1 photos for ALL 5 tests (10 photos each)")
print("  ✅ Part 3/4 question text + A/B/C/D for all tests")
print("  ✅ Group scripts for all tests")
print("  ✅ Answer keys for all 5 tests")
