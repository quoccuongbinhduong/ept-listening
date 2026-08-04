import json

with open('reading_answers.json', 'r', encoding='utf-8') as f:
    answers = json.load(f)

# Fix missing 101 for Test 1
if '101' not in answers.get('1', {}):
    answers['1']['101'] = 'A'

with open('reading_answers.json', 'w', encoding='utf-8') as f:
    json.dump(answers, f, indent=2)

with open('reading_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Fix missing 101 answer in reading_data.json
if '101' not in data['1']['answers']:
    data['1']['answers']['101'] = 'A'

# Add generic explanations for Test 3
exp_3 = {}
trans_3 = {}

for i in range(101, 201):
    q = str(i)
    ans = data['3']['answers'].get(q, '')
    if 101 <= i <= 150:
        exp_3[q] = f"Đáp án đúng là {ans}. Áp dụng các quy tắc điểm ngữ pháp và từ vựng cơ bản để chọn đáp án này."
        trans_3[q] = f"(Bản dịch chi tiết đang được cập nhật thêm...)"
    else:
        exp_3[q] = f"Đáp án đúng là {ans}. Thông tin và manh mối có thể tìm thấy trực tiếp trong đoạn văn."

data['3']['explanations'] = exp_3
data['3']['translations'] = trans_3

with open('reading_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Fixed 101 for Test 1 and updated generic explanations for Test 3')
