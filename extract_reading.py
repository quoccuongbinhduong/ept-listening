import fitz
import json

doc = fitz.open("Reading_0001.pdf")
text = ""
for page_num in range(min(5, doc.page_count)):  # Extract first 5 pages for preview
    page = doc.load_page(page_num)
    text += f"--- Page {page_num+1} ---\n"
    text += page.get_text()

with open("reading_preview.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Preview saved to reading_preview.txt")
