import fitz
import json
import base64
import os

pdf_path = r"D:\EPT\Listening\Listening_0001.pdf"
doc = fitz.open(pdf_path)

# Test pages (1-indexed based on my hypothesis)
# Test 1: 3-12
# Test 2: 15-24
# Test 3: 27-36
# Test 4: 39-48
# Test 5: 51-60
tests = {
    "1": range(2, 12),    # 0-indexed: 2 to 11
    "2": range(14, 24),   # 0-indexed: 14 to 23
    "3": range(26, 36),   # 0-indexed: 26 to 35
    "4": range(38, 48),   # 0-indexed: 38 to 47
    "5": range(50, 60),   # 0-indexed: 50 to 59
}

photos = {}

for test_num, page_range in tests.items():
    test_photos = {}
    for q_idx, page_num in enumerate(page_range):
        page = doc[page_num]
        images = page.get_images(full=True)
        if images:
            xref = images[0][0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            ext = base_image["ext"]
            b64 = base64.b64encode(image_bytes).decode('ascii')
            mime = f"image/{ext}" if ext != "jpg" else "image/jpeg"
            test_photos[str(q_idx + 1)] = f"data:{mime};base64,{b64}"
    photos[test_num] = test_photos

# Write to photos.json
out_path = r"D:\EPT\ept-deploy\photos.json"
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(photos, f)

print("Saved photos.json")
