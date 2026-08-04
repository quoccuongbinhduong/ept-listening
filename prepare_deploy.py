# Files cần thiết cho web app (không cần file .py, PDF, etc.)
# Chỉ copy: index.html, core.json, photos.json, Audio/, README.md

import os, shutil

SRC = r"D:\EPT\Listening"
DST = r"D:\EPT\ept-deploy"

KEEP_FILES = ["index.html", "core.json", "photos.json", "reading.html", "reading_data.json", "listening.html"]
KEEP_DIRS  = ["Audio", ".github"]

if not os.path.exists(DST):
    os.makedirs(DST)

for f in KEEP_FILES:
    src = os.path.join(SRC, f)
    if os.path.exists(src):
        shutil.copy2(src, os.path.join(DST, f))
        sz = os.path.getsize(os.path.join(DST, f))
        print(f"  Copied {f}: {sz//1024} KB")

for d in KEEP_DIRS:
    src = os.path.join(SRC, d)
    dst = os.path.join(DST, d)
    if os.path.exists(src):
        shutil.copytree(src, dst, dirs_exist_ok=True)
        files = os.listdir(dst)
        total = sum(os.path.getsize(os.path.join(dst,f)) for f in files)
        print(f"  Copied {d}/: {len(files)} files, {total//1024//1024} MB")

# Create README
readme = """# EPT Listening Practice – TDMU

Ứng dụng luyện nghe tiếng Anh cho kỳ thi EPT tại TDMU.

## Tính năng
- 5 bài Practice Test với 100 câu hỏi mỗi bài
- Audio player với điều chỉnh tốc độ
- Hiển thị ảnh Part 1 (Test 1)
- Script hội thoại Part 3 & 4
- Chấm điểm tự động và thống kê chi tiết

## Truy cập
Mở link GitHub Pages để bắt đầu luyện thi.
"""
with open(os.path.join(DST, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme)
print("  Created README.md")

# Total size
total_size = sum(
    os.path.getsize(os.path.join(dp, fn))
    for dp, dn, fns in os.walk(DST)
    for fn in fns
)
print(f"\nTotal deploy size: {total_size//1024//1024} MB")
print(f"Deploy folder: {DST}")
