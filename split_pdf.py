import fitz

pdf_path = "Reading_0001.pdf"
doc = fitz.open(pdf_path)

bounds = [
    (1, 13, 25), # Test 1: indices 13 to 25
    (2, 26, 39), # Test 2: indices 26 to 39
    (3, 40, 54), # Test 3: indices 40 to 54
    (4, 55, 68), # Test 4: indices 55 to 68
    (5, 69, 84)  # Test 5: indices 69 to 84
]

for test_num, start_idx, end_idx in bounds:
    # create a new empty PDF
    new_doc = fitz.open()
    new_doc.insert_pdf(doc, from_page=start_idx, to_page=end_idx)
    out_file = f"reading_test_{test_num}.pdf"
    new_doc.save(out_file)
    print(f"Saved {out_file} (Pages {start_idx+1}-{end_idx+1})")
