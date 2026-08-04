"""Split data.json into 2 files:
- core.json: answers + scripts (small, ~130KB)
- photos.json: base64 photos (large, ~1.1MB, loaded lazily)
"""
import json, os

with open('data.json', encoding='utf-8') as f:
    data = json.load(f)

core = {'answers': data['answers'], 'scripts': data['scripts']}
with open('core.json', 'w', encoding='utf-8') as f:
    json.dump(core, f, ensure_ascii=False, separators=(',',':'))
print(f"core.json: {os.path.getsize('core.json')//1024} KB")

photos = {'photos': data['photos']}
with open('photos.json', 'w', encoding='utf-8') as f:
    json.dump(photos, f, ensure_ascii=False, separators=(',',':'))
print(f"photos.json: {os.path.getsize('photos.json')//1024} KB")

# Quick validate
print("answers test 1:", list(core['answers']['1'].items())[:3])
print("scripts test 1 Q1 opts:", core['scripts']['1']['1']['options'])
