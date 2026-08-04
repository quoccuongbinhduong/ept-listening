import fitz
import pytesseract
from PIL import Image
import io

pdf_path = "Reading_0001.pdf"
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
doc = fitz.open(pdf_path)

out_text = ""
print("Starting OCR...")
# The reading tests are from page 14 to 85 (0-indexed 13 to 84)
# Let's extract first 2 pages to test
for i in range(13, 15):
    page = doc.load_page(i)
    # Render page to an image
    pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0))
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    
    # Run OCR
    text = pytesseract.image_to_string(img, lang='eng')
    out_text += f"\n--- Page {i+1} ---\n{text}"
    print(f"Done page {i+1}")

with open("ocr_test.txt", "w", encoding="utf-8") as f:
    f.write(out_text)
print("Finished OCR test.")
