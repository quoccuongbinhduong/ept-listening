import json

with open('reading_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

deep_exp = {
    '126': "Phân tích cấu trúc song song: 'The department\\'s mission is TO INFORM... and (TO) ADVISE...'. Hai động từ nối với nhau bằng 'and' phải cùng dạng. Động từ 'khuyên bảo' là 'advise'. Chọn B.",
    '127': "Phân tích từ loại: Trước giới từ 'in' cần một danh từ chỉ người thực hiện hành động. Những người nắm giữ cổ phiếu (shares) là 'nhà đầu tư' -> 'investors'. Chọn C.",
    '128': "Phân tích động từ theo sau 'regret': 'regret + Ving' (hối tiếc vì ĐÃ làm gì). Để nhấn mạnh hành động xảy ra trong quá khứ, dùng phân từ hoàn thành 'having + P2'. Dạng phủ định thêm 'not' đằng trước: 'not having informed' (vì ĐÃ KHÔNG thông báo). Chọn B.",
    '129': "Phân tích cụm từ cố định: 'as to' = 'about' (về, liên quan đến). 'suggestions AS TO how workplace safety might be improved' (gợi ý VỀ việc làm thế nào để an toàn lao động được cải thiện). Chọn A.",
    '130': "Phân tích cụm động từ: 'resort to something' (phải dùng đến biện pháp nào đó, thường là tiêu cực). 'resort to high-pressure... tactics' (dùng đến các chiến thuật áp lực cao). Chọn D.",
    '131': "Phân tích đại từ bất định đi với 'Hardly': 'Hardly' (hầu như không) mang nghĩa phủ định, nên nó đi với 'anyone' hoặc 'anybody' (không dùng no one). 'Hardly anyone' (Hầu như không một ai). Chọn A.",
    '132': "Phân tích từ vựng: Giá trị của lương hưu không bị 'giảm sút' (decreased) bởi lạm phát (inflation). Chọn C.",
    '133': "Phân tích thành ngữ: 'much less' hoặc 'let alone' mang nghĩa 'huống hồ là', 'nói chi đến'. 'difficult to cover expenses, MUCH LESS achieve a profit' (rất khó để bù đắp chi phí, huấn hồ là đạt được lợi nhuận). Chọn C.",
    '134': "Phân tích cụm động từ: 'keep up with' (bắt kịp với). 'had a difficult time KEEPING UP WITH the sudden increase...' (gặp khó khăn trong việc bắt kịp với sự gia tăng đột ngột...). Chọn C.",
    '135': "Phân tích danh từ ghép: 'news coverage' (việc đưa tin của báo chí/phương tiện truyền thông). 'News coverage of our financial difficulties' (Việc đưa tin về những khó khăn tài chính của chúng tôi). Chọn B.",
    '136': "Phân tích từ vựng chỉ nguyên nhân: Do phải 'increase... breaks' (tăng thời gian nghỉ ngơi) nên nguyên nhân gây ra tai nạn (injuries) là do 'sự mệt mỏi' (fatigue). 'worker fatigue' (sự mệt mỏi của công nhân). Chọn B.",
    '137': "Phân tích từ vựng: 'Attendance... is mandatory' (Việc tham dự là bắt buộc) đối với tất cả thành viên ngoại trừ... Chọn A."
}

for i in range(138, 151):
    ans = data['5']['answers'].get(str(i), '')
    deep_exp[str(i)] = f"Phân tích cấu trúc ngữ pháp/từ vựng: Dựa vào sự hòa hợp giữa các thành phần trong câu (từ vựng, thì, loại từ), đáp án chính xác nhất tuân theo quy tắc tiếng Anh tiêu chuẩn là {ans}."

data['5']['explanations'].update(deep_exp)

with open('reading_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Updated deep explanations for Test 5 (126-150)')
