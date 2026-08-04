import json

with open('reading_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data['1']['explanations'].update({
    '111': 'Cấu trúc "forget to do something" mang ý nghĩa là quên làm một việc gì đó cần phải làm. Do đó chọn "to stretch" (quên giãn cơ trước khi tập).',
    '112': 'Động từ đi chung với phương tiện giao thông thường là "take" (take a bus, take a train - đón xe buýt, đi tàu). Chủ ngữ số nhiều (Several students) nên dùng "take".',
    '113': "Câu hỏi ở thì hiện tại hoàn thành (Why haven't you + V3/ed), nên động từ chính cần chia ở dạng quá khứ phân từ là 'combed' (chải tóc)."
})

data['1']['translations'].update({
    '111': 'Lưng tôi bị đau vì tôi đã quên giãn cơ trước khi tập thể dục.',
    '112': 'Một vài học sinh từ vùng ngoại ô đi xe buýt đến trường.',
    '113': 'Tại sao bạn vẫn chưa chải tóc vậy?'
})

with open('reading_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Updated 111-113')
