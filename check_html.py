import os
f = 'index.html'
size = os.path.getsize(f)
print(f'File size: {size:,} bytes ({size/1024:.1f} KB)')
with open(f, encoding='utf-8') as fh:
    content = fh.read()
checks = [
    ('DOCTYPE', '<!DOCTYPE html>' in content),
    ('Audio element', 'audio-el' in content),
    ('ANSWERS object', 'const ANSWERS' in content),
    ('5 tests in ANSWERS', content.count('"1":"B"') >= 1),
    ('Submit function', 'submitExam' in content),
    ('Result screen', 'screen-result' in content),
    ('Speed control', 'setSpeed' in content),
    ('localStorage', 'localStorage' in content),
    ('Audio files paths', 'Practice Test 1.mp3' in content),
]
all_ok = True
for name, ok in checks:
    print(f'  {"OK" if ok else "FAIL"} {name}')
    if not ok:
        all_ok = False
print()
print('All checks passed!' if all_ok else 'Some checks failed!')
