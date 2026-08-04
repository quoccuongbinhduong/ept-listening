import fitz
import re

pdf_path = r"D:\EPT\Listening\Listening_0001.pdf"
doc = fitz.open(pdf_path)

current_test = 0
image_mapping = {}

for i in range(len(doc)):
    page = doc[i]
    text = page.get_text()
    
    # Identify test boundaries
    m = re.search(r'PRACTICE\s+TEST\s+(\d+)', text, re.IGNORECASE)
    if m:
        current_test = int(m.group(1))
    
    images = page.get_images(full=True)
    if images:
        if current_test not in image_mapping:
            image_mapping[current_test] = []
        image_mapping[current_test].extend(images)

for test, imgs in image_mapping.items():
    print(f"Test {test}: {len(imgs)} images")
