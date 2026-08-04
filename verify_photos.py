"""Quick check: extract and save sample photos from each test to verify correctness"""
import fitz, base64
from PIL import Image
from io import BytesIO
import os

doc = fitz.open('Listening_0001.pdf')
out = 'photo_check'
os.makedirs(out, exist_ok=True)

PAGES_PER_TEST = 12
PHOTO_OFFSETS = range(2, 7)

for test_num in range(1, 6):
    base_page = (test_num - 1) * PAGES_PER_TEST
    page_idx = base_page + 2  # first photo page
    page = doc[page_idx]
    mat = fitz.Matrix(1.5, 1.5)
    pix = page.get_pixmap(matrix=mat, alpha=False)
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    W, H = img.width, img.height
    pad_x = int(W * 0.04)
    # Save both crops for first photo page of each test
    crop1 = img.crop((pad_x, int(H*0.04), W-pad_x, int(H*0.48)))
    crop2 = img.crop((pad_x, int(H*0.52), W-pad_x, int(H*0.96)))
    crop1.save(f'{out}/test{test_num}_q1.jpg')
    crop2.save(f'{out}/test{test_num}_q2.jpg')
    print(f"Test {test_num}: saved Q1 and Q2 samples")

print("Done! Check photo_check/ folder")
