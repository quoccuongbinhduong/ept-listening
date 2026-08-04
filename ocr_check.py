import fitz
import pytesseract
from PIL import Image
import io

pdf_path = r"D:\EPT\Listening\Listening_0001.pdf"
doc = fitz.open(pdf_path)

for i in range(15):  # Check first 15 pages
    page = doc[i]
    images = page.get_images(full=True)
    if images:
        xref = images[0][0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        img = Image.open(io.BytesIO(image_bytes))
        
        # OCR the image to see text
        text = pytesseract.image_to_string(img).strip()
        
        # Print a short summary of the text
        print(f"Page {i+1}:")
        print(text[:100].replace('\n', ' '))
        print("-" * 20)
