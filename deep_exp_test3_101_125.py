import json

with open('reading_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

deep_exp = {
    '101': "Phân tích liên từ: Hai mệnh đề có ý nghĩa trái ngược nhau: 'Tôi thích trà' (I like tea) và 'vợ tôi thì không' (my wife doesn\\'t). Liên từ nối hai vế tương phản là 'but' (nhưng). Do đó chọn C.",
    '102': "Phân tích giới từ đi kèm tính từ: Cấu trúc bị động hoặc tính từ miêu tả sự nổi tiếng/được biết đến đối với một đối tượng nào đó: 'be known TO somebody' (được biết đến bởi ai). 'known by' thường dùng để nhận biết qua đặc điểm nào đó, nhưng khi nhắc đến đối tượng biết đến tác phẩm/người thì dùng 'known to'. Chọn B.",
    '103': "Phân tích thì bị động: Có từ 'by the students' báo hiệu câu bị động. Động từ to-be là 'is', chỗ trống cần một yếu tố tạo thành bị động của thì hiện tại tiếp diễn (is being + P2) hoặc bị động cơ bản (is + P2). Trong các đáp án, 'being' phù hợp tạo thành 'is being discussed' (đang được thảo luận). Chọn C.",
    '104': "Phân tích liên từ: Hai mệnh đề là 'nền kinh tế đang bùng nổ' và 'doanh số của chúng ta đang tăng lên'. Mối quan hệ là Nguyên nhân - Kết quả. Từ chỉ nguyên nhân đứng ở đầu câu là 'Because' (Bởi vì). Chọn B.",
    '105': "Phân tích câu hỏi đuôi: Mệnh đề chính là 'We have met' (thì Hiện tại hoàn thành, khẳng định). Do đó phần câu hỏi đuôi phải ở dạng phủ định của thì HTHT, sử dụng trợ động từ 'have' + not -> 'haven\\'t we'. Chọn C.",
    '106': "Phân tích bị động với động từ khuyết thiếu: Chủ ngữ là 'The report' (bản báo cáo - vật), động từ 'type' (đánh máy). Báo cáo phải 'được đánh máy' (bị động). Cấu trúc bị động sau modal verb (must): 'must + BE + P2'. Do đó chọn C (be typed).",
    '107': "Phân tích rút gọn mệnh đề quan hệ chủ động: Câu gốc là 'We\\'ll read a report WHICH EXPLAINS the new business'. Khi rút gọn mệnh đề quan hệ mang nghĩa chủ động (bản báo cáo đó giải thích...), ta dùng V-ing. Rút gọn thành 'explaining'. Chọn D.",
    '108': "Phân tích cấu trúc chủ ngữ giả: Cấu trúc 'It is + tính từ + TO V' (Thật là ... để làm gì). Ở đây là 'It is necessary TO THINK of the problem' (Cần thiết phải suy nghĩ về vấn đề này). Chọn B.",
    '109': "Phân tích cấu trúc động từ chỉ giác quan: Động từ 'hear' (nghe) có hai cấu trúc: 'hear sb DO sth' (nghe thấy toàn bộ hành động) hoặc 'hear sb DOING sth' (nghe thấy hành động đang diễn ra). Trong các đáp án có 'ringing' (V-ing) là phù hợp nhất (nghe thấy chuông đang reo). Chọn D.",
    '110': "Phân tích giới từ + V-ing: 'by' là giới từ. Theo nguyên tắc, sau giới từ (in, on, at, by, for...) nếu là động từ thì phải thêm đuôi -ing (V-ing). 'by processing data' (bằng cách xử lý dữ liệu). Chọn C.",
    '111': "Phân tích cấu trúc khuyên bảo/yêu cầu: Động từ 'tell' (quá khứ là told) đi với tân ngữ và động từ nguyên mẫu có to. Cấu trúc 'tell sb TO DO sth' (Bảo ai làm gì). 'told Jack to come'. Chọn A.",
    '112': "Phân tích câu mệnh lệnh phủ định: Để bắt đầu một câu mệnh lệnh yêu cầu ai đó KHÔNG làm gì, ta dùng 'Don\\'t + V(nguyên mẫu)'. 'Don\\'t say such a thing again' (Đừng nói những điều như vậy nữa). Chọn B.",
    '113': "Phân tích động từ 'enter': Khi mang nghĩa đi vào một không gian vật lý (căn phòng, tòa nhà), động từ 'enter' KHÔNG đi kèm với giới từ (như in, into). Cấu trúc: 'enter + Nơi chốn'. 'entered the classroom'. Chọn A.",
    '114': "Phân tích mệnh đề kết quả dạng V-ing: Phân từ hiện tại (V-ing) thường được dùng ở cuối câu, cách bằng dấu phẩy, để diễn tả kết quả hoặc một hành động nối tiếp theo sau hành động chính. 'Máy bay rời đi lúc 9 giờ, VÀ đến nơi lúc 11 giờ' -> 'arriving in New York...'. Chọn B.",
    '115': "Phân tích động từ theo sau: Động từ 'plan' (lên kế hoạch) luôn đi theo sau bởi động từ nguyên mẫu có 'to'. Cấu trúc 'plan TO DO sth'. 'planning to offer'. Chọn A.",
    '116': "Phân tích giới từ chỉ đối tượng hưởng lợi: Để nói làm một việc gì đó CHO ai (mang lại lợi ích cho họ), ta dùng giới từ 'for'. 'sing a song FOR the children' (hát một bài cho bọn trẻ). Chọn B.",
    '117': "Phân tích cấu trúc cầu khiến: Động từ 'make' mang nghĩa sai khiến có cấu trúc: 'make somebody DO something' (bắt/làm cho ai đó phải làm gì). Động từ theo sau bắt buộc ở dạng nguyên thể không to (V). 'makes us laugh' (làm chúng tôi cười). Chọn C.",
    '118': "Phân tích câu cảm thán: Cấu trúc câu cảm thán với What: 'What + (a/an) + adj + Noun + S + V!'. Trong câu có cụm danh từ 'beautiful women' (số nhiều), nên ta dùng 'What beautiful women they are!'. Chọn A.",
    '119': "Phân tích cấu trúc 'too... to': Cấu trúc 'too + adj + TO V' mang nghĩa 'quá... đến nỗi không thể làm gì'. Tuy nhiên, 'busy' còn có một cấu trúc riêng là 'busy DOING sth' (bận rộn làm gì). Ở đây, cấu trúc 'too busy TO EAT lunch' (quá bận để có thể ăn trưa) phù hợp nhất với cấu trúc chuẩn 'too... to'. Chọn B.",
    '120': "Phân tích động từ theo sau: Động từ 'decide' (quyết định) luôn đi kèm với động từ nguyên mẫu có 'to'. Cấu trúc 'decide TO DO sth' (quyết định làm gì). 'decided to do'. Chọn B.",
    '121': "Phân tích động từ nguyên thể bổ nghĩa cho danh từ: Khi muốn nói 'những nơi ĐỂ thăm quan', động từ 'see' đóng vai trò bổ nghĩa cho danh từ 'places' đứng trước nó, ta dùng dạng TO V. 'places to see' (những nơi để thăm). Chọn C.",
    '122': "Phân tích động từ nguyên thể bổ nghĩa cho danh từ: Tương tự câu 121, 'benches' (băng ghế) để 'ngồi lên' (sit on). Ta dùng động từ nguyên thể có 'to' để bổ nghĩa. 'benches to sit on' (những băng ghế để ngồi). Chọn C.",
    '123': "Phân tích cấu trúc bị động truyền khiến (Causative): Khi có một việc gì đó tồi tệ xảy ra với tài sản của mình (bị trộm), ta dùng cấu trúc 'have + Object (vật) + P2'. 'have your passport STOLEN' (bị trộm mất hộ chiếu). 'stolen' là phân từ 2 của steal. Chọn C.",
    '124': "Phân tích động từ theo sau: Động từ 'mind' (phiền lòng, ngại) luôn yêu cầu động từ theo sau ở dạng V-ing. Cấu trúc 'mind DOING sth'. 'don\\'t mind being alone' (không ngại việc ở một mình). Chọn B.",
    '125': "Phân tích động từ nguyên thể chỉ mục đích: Để trả lời cho câu hỏi 'làm gì đó ĐỂ LÀM GÌ', ta dùng động từ nguyên mẫu có 'to' (To V). 'went to Busan TO VISIT' (đến Busan để thăm...). Chọn A."
}

data['3']['explanations'].update(deep_exp)

with open('reading_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Updated deep explanations for Test 3 (101-125)')
