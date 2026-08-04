"""
Better photo crop - detect actual photo boundaries using pixel analysis
"""
import fitz, base64, json, os
from PIL import Image, ImageChops
from io import BytesIO

doc = fitz.open('LISTENING PRACTICE-1.pdf')
PHOTO_PAGES = {2:(1,2), 3:(3,4), 4:(5,6), 5:(7,8), 6:(9,10)}
photos_b64 = {}
os.makedirs('images/part1', exist_ok=True)

def find_content_box(img, margin=20):
    """Find tightest bounding box of non-white content."""
    gray = img.convert('L')
    # Find rows/cols that are not all white (threshold < 250)
    import numpy as np
    arr = np.array(gray)
    # rows with dark pixels
    row_dark = (arr < 240).any(axis=1)
    col_dark  = (arr < 240).any(axis=0)
    rows = np.where(row_dark)[0]
    cols = np.where(col_dark)[0]
    if len(rows)==0 or len(cols)==0:
        return (0, 0, img.width, img.height)
    top    = max(0, rows[0] - margin)
    bottom = min(img.height, rows[-1] + margin)
    left   = max(0, cols[0] - margin)
    right  = min(img.width, cols[-1] + margin)
    return (left, top, right, bottom)

def find_photos_on_page(full_img):
    """Split page into top and bottom photo, trimming white space."""
    import numpy as np
    W, H = full_img.width, full_img.height
    arr = (np.array(full_img.convert('L')) < 235).astype(int)
    
    # Find the vertical midpoint gap (most white rows in the middle)
    row_darkness = arr.sum(axis=1)
    
    # Find the gap between the two photos (section of low darkness)
    mid_search_start = H // 3
    mid_search_end   = 2 * H // 3
    mid_region = row_darkness[mid_search_start:mid_search_end]
    
    # Find the darkest gap = minimum darkness region
    gap_idx = mid_region.argmin() + mid_search_start
    
    # Search around gap_idx for best split (white band)
    best_split = gap_idx
    for r in range(max(0, gap_idx-60), min(H, gap_idx+60)):
        if row_darkness[r] < row_darkness[best_split]:
            best_split = r
    
    # Split and trim each half
    top_img = full_img.crop((0, 0, W, best_split))
    bot_img = full_img.crop((0, best_split, W, H))
    
    top_box = find_content_box(top_img, margin=8)
    bot_box = find_content_box(bot_img, margin=8)
    
    top_cropped = top_img.crop(top_box)
    bot_cropped = bot_img.crop(bot_box)
    
    return top_cropped, bot_cropped

for page_num, (q1, q2) in PHOTO_PAGES.items():
    page = doc[page_num-1]
    mat  = fitz.Matrix(2.0, 2.0)
    pix  = page.get_pixmap(matrix=mat, alpha=False)
    full_img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    
    top_img, bot_img = find_photos_on_page(full_img)
    
    for qn, img in [(q1, top_img), (q2, bot_img)]:
        buf = BytesIO()
        img.save(buf, format='JPEG', quality=82)
        b64 = base64.b64encode(buf.getvalue()).decode()
        photos_b64[str(qn)] = f"data:image/jpeg;base64,{b64}"
        img.save(f'images/part1/q{qn}_v2.jpg', quality=82)
        print(f"  Q{qn}: {img.size}")

# Save
with open('photos_b64.json', 'w') as f:
    json.dump(photos_b64, f)
print(f"Saved {len(photos_b64)} photos")
