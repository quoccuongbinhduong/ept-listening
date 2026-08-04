import json

with open('reading_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

deep_exp = {
    '114': 'Phân tích cấu trúc: Động từ "tell" (bảo, kể) luôn đi kèm với tân ngữ chỉ người (me) và một động từ nguyên mẫu có "to" theo cấu trúc: "tell somebody TO DO something" (Bảo ai đó làm việc gì). Ở đây, câu có nghĩa là "Sếp bảo tôi phải hoàn thành...". Vì vậy, đáp án B (to finish) là đáp án duy nhất đúng ngữ pháp. Các đáp án khác (finish - nguyên mẫu không to, finishing - danh động từ) đều sai cấu trúc của "tell".',
    '115': 'Phân tích cấu trúc chủ ngữ giả "It": Khi muốn nhận xét về một hành động, ta dùng cấu trúc: "It is + Tính từ + TO DO something" (Thật là [tính từ] để làm việc gì đó). Trong câu này: It is difficult (Thật là khó) + to row (để chèo thuyền). "row" ở đây đóng vai trò là động từ. Vì vậy, ta phải chọn C (to row). A sai vì thiếu "to", B sai vì là thì quá khứ.',
    '116': 'Phân tích từ loại và cấu trúc: Danh từ "time" (thời gian) khi muốn diễn đạt ý "thời gian để làm một việc gì đó", ta phải dùng động từ nguyên mẫu có "to" bổ nghĩa cho danh từ đó. Cấu trúc: "have time TO DO something" (có thời gian để làm gì). Do đó, đáp án đúng là C (to look). Câu mang ý nghĩa: "Tôi không có thời gian để tìm kiếm chiếc xe rẻ nhất".',
    '117': 'Phân tích nghĩa của từ: Câu này kiểm tra từ vựng. "Borrow" nghĩa là đi mượn của ai đó (chủ ngữ là người đi mượn). "Lend" nghĩa là cho ai đó mượn (chủ ngữ là người cho mượn). Trong câu "Could you ___ me your umbrella?" (Bạn có thể ___ tôi cái ô của bạn không?), chủ ngữ là "you" (bạn), người nhận là "me" (tôi). Nên động từ phải mang nghĩa "cho mượn". Do đó chọn B (lend).',
    '118': "Phân tích thì của câu: Câu chứa 'During the day' diễn tả một sự thật hoặc thói quen, nên dùng thì Hiện tại đơn. Chủ ngữ là 'they' (ngôi thứ 3 số nhiều). Trong thì hiện tại đơn, phủ định của động từ thường đối với chủ ngữ số nhiều phải mượn trợ động từ 'do' + not = 'don\\'t'. Do đó chọn D. A sai vì dùng cho số ít. B sai vì là quá khứ.",
    '119': 'Phân tích sự hòa hợp Chủ ngữ - Động từ: Chủ ngữ "All of the people there" có từ khóa chính là "people" (những người - danh từ đếm được số nhiều). Do đó, động từ to-be phải chia ở số nhiều. Trong 4 đáp án: A (were) là số nhiều quá khứ, B (is) là số ít, C (be) là nguyên mẫu, D (was) là số ít quá khứ. Chỉ có A thỏa mãn điều kiện số nhiều.',
    '120': 'Phân tích giới từ chỉ phương tiện: Khi nói di chuyển bằng phương tiện giao thông (xe buýt, tàu hỏa, máy bay) mà không có mạo từ (a/the) hay tính từ sở hữu đứng trước phương tiện, ta luôn dùng giới từ "by". Cấu trúc: "go by train" (đi bằng tàu hỏa). Do đó chọn A.',
    '121': "Phân tích cấu trúc khuyên nhủ: Cụm từ 'I\\'d better' là viết tắt của 'I had better'. Cấu trúc 'had better + V (nguyên mẫu không to)' mang ý nghĩa khuyên nhủ 'tốt hơn hết là nên làm gì'. Động từ theo sau bắt buộc phải ở dạng nguyên thể. Do đó chọn A (go).",
    '122': 'Phân tích từ vựng: "Bring" mang ý nghĩa là mang cái gì đó từ xa đến gần người nói (mang lại cho tôi). "Take" là mang cái gì đó từ gần người nói đi xa. Ở đây câu yêu cầu "Bạn có thể mang cho tôi chiếc áo màu đỏ được không?" nên phải dùng D (bring).',
    '123': 'Phân tích thì Hiện tại hoàn thành: Động từ trong câu là "have solved" (thì hiện tại hoàn thành). Trạng từ "already" (đã... rồi) thường đứng giữa trợ động từ "have/has" và động từ chính (phân từ 2) để nhấn mạnh hành động đã hoàn tất. Do đó chọn A.',
    '124': 'Phân tích giới từ chỉ thời gian trong tương lai: Để diễn tả một việc sẽ xảy ra "trong vòng bao nhiêu thời gian nữa" tính từ hiện tại (ở thì tương lai), ta dùng giới từ "in" + khoảng thời gian. "In a few minutes" nghĩa là "trong vài phút nữa". Do đó chọn A.',
    '125': "Phân tích giới từ thời gian: Giới từ 'by' đi với một mốc thời gian có nghĩa là 'trước hoặc chậm nhất là vào lúc đó'. 'By six o\\'clock' nghĩa là 'trước 6 giờ'. Trong ngữ cảnh 'sáng mai bạn phải thức dậy...', dùng 'by' hợp lý nhất. Do đó chọn B.",
    '126': 'Phân tích mệnh đề quan hệ: Động từ gốc là "speak to somebody" (nói chuyện với ai). Khi biến thành mệnh đề quan hệ thay thế cho người (The man) làm tân ngữ, ta dùng "whom". Đồng thời trong lối văn trang trọng, giới từ "to" được đảo lên trước "whom" thành "to whom". Do đó chọn C.',
    '127': 'Phân tích từ loại: Trong câu hỏi "Is the store ___ on Sundays?", ta đã có động từ to-be là "Is". Sau động từ to-be cần một tính từ. Từ "open" vừa là động từ (mở cửa) vừa là tính từ (trạng thái đang mở cửa). Vì thế ta chọn A (open - tính từ).',
    '128': 'Phân tích từ loại: Câu có chủ ngữ "He", động từ to-be "is" và trạng từ chỉ mức độ "very". Vị trí cần điền bắt buộc phải là một Tính từ để miêu tả tính cách. "Patient" (A) là tính từ (kiên nhẫn). "Patience" (B) là danh từ. Do đó chọn A.',
    '129': 'Phân tích ngữ cảnh: Mệnh đề trước là "Neither of them knows how to cook" (Không ai trong số họ biết nấu ăn). Dựa vào logic nhân quả (so - vì vậy), vì không biết nấu ăn nên họ sẽ THƯỜNG XUYÊN đi ăn ngoài. Trạng từ phù hợp nhất về nghĩa là "often" (thường xuyên). Các từ seldom, rarely, never mang nghĩa phủ định là sai logic.',
    '130': 'Phân tích giới từ chỉ phương hướng: Động từ "went" (quá khứ của go) khi chỉ sự di chuyển đến một địa điểm (Guam) luôn đi kèm với giới từ "to". Cấu trúc: "go to + địa điểm". Do đó chọn B.'
}

data['1']['explanations'].update(deep_exp)

with open('reading_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Updated deep explanations for 114-130')
