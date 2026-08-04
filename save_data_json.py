"""
Create data.json - separate data file loaded by fetch() instead of embedded in HTML
"""
import json, os, re, pdfplumber, fitz, base64
from PIL import Image
from io import BytesIO
import numpy as np

# ── Answers ─────────────────────────────────────────────────
answers = {}
with pdfplumber.open('TAI LIEU EPT-TDMU Đáp án.pdf') as pdf:
    cur = None; inL = True
    for page in pdf.pages:
        txt = page.extract_text()
        if not txt: continue
        for line in txt.split('\n'):
            if 'A. LISTENING' in line: inL = True; continue
            if 'B. READING'   in line: inL = False; continue
            m = re.match(r'Practice Test (\d+)', line.strip())
            if m:
                cur = int(m.group(1))
                if inL and cur not in answers: answers[cur] = {}
                continue
            if cur and inL:
                for num, ans in re.findall(r'(\d+)\s+([ABCD])', line):
                    n = int(num)
                    if n <= 100: answers[cur][n] = ans

answers_json = {str(t): {str(k): v for k,v in a.items()} for t,a in answers.items()}
print(f"Answers: {sum(len(v) for v in answers_json.values())} total")

# ── Scripts ──────────────────────────────────────────────────
with open('scripts_structured.json', encoding='utf-8') as f:
    scripts_json = json.load(f)
print(f"Scripts: {sum(len(v) for v in scripts_json.values())} questions")

# ── Photos ───────────────────────────────────────────────────
def find_photos_on_page(full_img):
    W, H = full_img.width, full_img.height
    arr = (np.array(full_img.convert('L')) < 235).astype(int)
    row_darkness = arr.sum(axis=1)
    mid_s, mid_e = H//3, 2*H//3
    mid_region = row_darkness[mid_s:mid_e]
    gap = mid_region.argmin() + mid_s
    best = gap
    for r in range(max(0,gap-60), min(H,gap+60)):
        if row_darkness[r] < row_darkness[best]: best = r
    
    def trim(img):
        a = (np.array(img.convert('L')) < 240).astype(int)
        rows = np.where(a.sum(axis=1))[0]
        cols = np.where(a.sum(axis=0))[0]
        if len(rows)==0 or len(cols)==0: return img
        m=10
        return img.crop((max(0,cols[0]-m), max(0,rows[0]-m),
                         min(img.width,cols[-1]+m), min(img.height,rows[-1]+m)))
    
    top = trim(full_img.crop((0,0,W,best)))
    bot = trim(full_img.crop((0,best,W,H)))
    return top, bot

doc = fitz.open('LISTENING PRACTICE-1.pdf')
PHOTO_PAGES = {2:(1,2), 3:(3,4), 4:(5,6), 5:(7,8), 6:(9,10)}
photos = {}

for page_num, (q1, q2) in PHOTO_PAGES.items():
    page = doc[page_num-1]
    mat  = fitz.Matrix(2.0, 2.0)
    pix  = page.get_pixmap(matrix=mat, alpha=False)
    full = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    t, b = find_photos_on_page(full)
    for qn, img in [(q1,t),(q2,b)]:
        buf = BytesIO()
        img.save(buf, 'JPEG', quality=80)
        photos[str(qn)] = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
        print(f"  Photo Q{qn}: {img.size}")

# ── Save data.json ───────────────────────────────────────────
data = {'answers': answers_json, 'scripts': scripts_json, 'photos': photos}
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, separators=(',',':'))

sz = os.path.getsize('data.json')
print(f"\nSaved data.json: {sz//1024} KB")
