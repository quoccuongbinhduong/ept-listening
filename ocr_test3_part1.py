import fitz
import pytesseract
from PIL import Image

pdf_path = "Reading_0001.pdf"
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
doc = fitz.open(pdf_path)

out_text = ""
for i in range(41, 45): # Pages 42 to 45 (1-indexed)
    page = doc.load_page(i)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0))
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    text = pytesseract.image_to_string(img, lang='eng')
    out_text += f"\n--- Page {i+1} ---\n{text}"
    print(f"Done page {i+1}")

with open("ocr_test3_part1.txt", "w", encoding="utf-8") as f:
    f.write(out_text)
print("Finished OCR for Test 3 Part 1.")
