import fitz
import pytesseract
from PIL import Image

pdf_path = "Reading_0001.pdf"
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
doc = fitz.open(pdf_path)

# OCR Test 4
out_text4 = ""
for i in range(55, 59): # Pages 56 to 59 (1-indexed)
    page = doc.load_page(i)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0))
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    text = pytesseract.image_to_string(img, lang='eng')
    out_text4 += f"\n--- Page {i+1} ---\n{text}"
    print(f"Done page {i+1}")

with open("ocr_test4_part1.txt", "w", encoding="utf-8") as f:
    f.write(out_text4)
print("Finished OCR for Test 4 Part 1.")

# OCR Test 5
out_text5 = ""
for i in range(69, 73): # Pages 70 to 73 (1-indexed)
    page = doc.load_page(i)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0))
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    text = pytesseract.image_to_string(img, lang='eng')
    out_text5 += f"\n--- Page {i+1} ---\n{text}"
    print(f"Done page {i+1}")

with open("ocr_test5_part1.txt", "w", encoding="utf-8") as f:
    f.write(out_text5)
print("Finished OCR for Test 5 Part 1.")
