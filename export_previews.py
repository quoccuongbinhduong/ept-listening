"""
Export tất cả 60 trang PDF thành ảnh nhỏ để xem cấu trúc
"""
import fitz
from PIL import Image
from io import BytesIO
import os

doc = fitz.open(r'D:\EPT\Listening\Listening_0001.pdf')
out_dir = r'D:\EPT\Listening\page_previews'
os.makedirs(out_dir, exist_ok=True)

for i in range(len(doc)):
    page = doc[i]
    # Render at low res just for preview
    mat = fitz.Matrix(0.3, 0.3)
    pix = page.get_pixmap(matrix=mat, alpha=False)
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    img.save(f"{out_dir}/page_{i+1:02d}.jpg", "JPEG", quality=60)

print(f"Saved {len(doc)} preview images to {out_dir}")
