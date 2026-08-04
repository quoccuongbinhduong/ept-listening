import os
print("=== EPT APP - FINAL FILE SIZES ===")
files = [
    ('index.html', 'Web App chinh'),
    ('scripts_structured.json', 'Script data'),
    ('photos_b64.json', 'Photos data'),
    ('START_SERVER.bat', 'Server launcher'),
]
for f, desc in files:
    if os.path.exists(f):
        print(f"  {f}: {os.path.getsize(f)//1024} KB  ({desc})")

print()
print("=== AUDIO FILES ===")
for f in sorted(os.listdir('Audio')):
    sz = os.path.getsize(f'Audio/{f}')
    print(f"  {f}: {sz//1024//1024} MB")

print()
print("=== PHOTOS (PART 1) ===")
for f in sorted(os.listdir('images/part1')):
    if 'v2' in f:
        print(f"  {f}: {os.path.getsize('images/part1/'+f)//1024} KB")

print()
print("=== QUICK VALIDATION ===")
with open('index.html', encoding='utf-8') as fh:
    html = fh.read()

checks = [
    ('Photos embedded (base64)',   'data:image/jpeg;base64,' in html),
    ('Script options embedded',    '(A) They' in html),
    ('Group scripts (hoi thoai)',  'Man:' in html or 'Woman:' in html),
    ('5 answer keys',              '"5":{"1":' in html),
    ('Audio player',               'btn-play' in html),
    ('Part tabs',                  'filterPart' in html),
    ('Result screen',              'screen-result' in html),
    ('Speed control',              'setSpeed' in html),
]
for name, ok in checks:
    print(f"  {'OK' if ok else 'FAIL'}  {name}")
