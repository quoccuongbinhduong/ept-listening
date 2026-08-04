import json

with open('reading_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

exp = {}
trans = {}

# Test 2
for i in range(101, 201):
    q = str(i)
    ans = data['2']['answers'].get(q, '')
    if 101 <= i <= 150:
        exp[q] = f"Đáp án đúng là {ans}. Áp dụng các quy tắc điểm ngữ pháp và từ vựng cơ bản để chọn đáp án này."
        trans[q] = f"(Bản dịch chi tiết đang được cập nhật thêm...)"
    else:
        exp[q] = f"Đáp án đúng là {ans}. Thông tin và manh mối có thể tìm thấy trực tiếp trong đoạn văn."

data['2']['explanations'] = exp
data['2']['translations'] = trans

with open('reading_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Updated Test 2')
