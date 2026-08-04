import fitz

pdf_path = r"D:\EPT\Listening\Listening_0001.pdf"
doc = fitz.open(pdf_path)

img_count = 0
for i in range(len(doc)):
    page = doc[i]
    images = page.get_images(full=True)
    if images:
        print(f"Page {i+1}: {len(images)} images")
        img_count += len(images)

print(f"Total images: {img_count}")
