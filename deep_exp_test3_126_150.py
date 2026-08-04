import json

with open('reading_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

deep_exp = {
    '126': "Phân tích cụm từ cố định (Collocation): Để diễn tả thức ăn bị ôi thiu, hỏng, tiếng Anh dùng cụm 'go bad' (quá khứ là went bad). Không dùng 'badly' vì sau 'go' mang nghĩa chuyển đổi trạng thái phải là tính từ. Chọn A.",
    '127': "Phân tích rút gọn mệnh đề quan hệ dạng bị động: Câu đầy đủ là 'There was a tree WHICH WAS BLOWN down' (Có một cái cây bị thổi ngã). Khi rút gọn mệnh đề quan hệ mang nghĩa bị động, ta giữ lại phân từ 2 (P2). P2 của blow là blown. Chọn D.",
    '128': "Phân tích cấu trúc chủ ngữ giả: Cấu trúc 'It is + tính từ + FOR somebody + TO V'. Ở đây là 'It is easy FOR him to swim...' (Thật dễ dàng cho anh ấy để bơi...). Chọn A.",
    '129': "Phân tích động từ truyền khiến: Cấu trúc 'let somebody DO something' (để cho ai đó làm gì / cho ai đó biết). Động từ sau 'let' luôn là nguyên thể không to (V). 'let you know' (cho bạn biết). Chọn B.",
    '130': "Phân tích giới từ đi kèm tính từ: Tính từ 'satisfied' (hài lòng, thỏa mãn) luôn đi kèm với giới từ 'with'. 'satisfied with his salary' (hài lòng với mức lương của anh ấy). Chọn C.",
    '131': "Phân tích sự hòa hợp Chủ ngữ - Động từ: Chủ ngữ là 'A trip to another country' (Một chuyến đi tới quốc gia khác). Từ khóa chính là 'A trip' (số ít). Do đó động từ 'need' phải chia thêm 's' thành 'needs'. Chọn B.",
    '132': "Phân tích Danh động từ làm chủ ngữ: Khi một hành động đóng vai trò làm chủ ngữ trong câu, ta phải dùng Danh động từ (V-ing). 'Going there alone' (Việc đi đến đó một mình) đóng vai trò chủ ngữ số ít, đi với động từ to-be 'was'. Chọn B.",
    '133': "Phân tích liên từ: Hai mệnh đề có quan hệ nguyên nhân - kết quả. 'Lisa đang đói' (kết quả) VÌ 'cô ấy không ăn sáng' (nguyên nhân). Liên từ chỉ nguyên nhân là 'because'. Chọn A.",
    '134': "Phân tích liên từ trái ngược: Hai vế là 'It\\'s a nice house' (Đó là một ngôi nhà đẹp) và 'it hasn\\'t got a garage' (nó không có nhà để xe). Hai ý trái ngược nhau (đẹp NHƯNG thiếu tiện nghi), ta dùng 'but'. Chọn D.",
    '135': "Phân tích đại từ nghi vấn làm chủ ngữ: Khi 'Who' đóng vai trò làm chủ ngữ đi hỏi, động từ theo sau nó được chia ở ngôi thứ 3 số ít. Trong ngữ cảnh câu, ta dùng động từ 'has' (Ai có...). Chọn B.",
    '136': "Phân tích từ loại sau to-be: Chỗ trống đứng sau động từ to-be 'is', cần một danh từ chỉ nghề nghiệp hoặc danh tính để giới thiệu. 'a famous actress' (một nữ diễn viên nổi tiếng) là cụm danh từ phù hợp. Chọn B.",
    '137': "Phân tích động từ liên kết (Linking verb): 'Get' (trở nên) là một linking verb. Theo sau linking verb phải là một Tính Từ, không phải trạng từ. Do đó ta dùng 'dark' (tối). 'getting dark' (trời đang trở tối). Chọn A.",
    '138': "Phân tích cấu trúc 'There is/are': Chủ ngữ thực sự đứng sau động từ to-be là 'students' (số nhiều). Cấu trúc câu hỏi: 'How many students ARE there...?'. Chọn D.",
    '139': "Phân tích động từ theo sau: Động từ 'want' (muốn) luôn đi với động từ nguyên mẫu có 'to'. Cấu trúc 'want TO DO sth'. Ở đây là 'want to see' (muốn xem). Chọn C.",
    '140': "Phân tích tân ngữ: Sau động từ 'loves' cần một tân ngữ để nhận hành động yêu thương. Tân ngữ chỉ người đại diện cho nam giới là 'him'. 'She loves him' (Cô ấy yêu anh ấy). Chọn B.",
    '141': "Phân tích danh từ số nhiều: Động từ 'send' (gửi) đi với tân ngữ người (them) và tân ngữ vật (presents). Vì không có mạo từ 'a' nên danh từ 'present' đếm được phải để ở số nhiều 'presents' (những món quà). Chọn C.",
    '142': "Phân tích cấu trúc chủ ngữ giả: Cấu trúc 'It is (not) necessary TO DO sth' (Không cần thiết phải làm gì). Do đó ta dùng TO V. Chọn B (to go).",
    '143': "Phân tích động từ bổ nghĩa đại từ bất định: Để nói 'một thứ gì đó ĐỂ uống', ta dùng động từ nguyên thể có 'to' để bổ nghĩa cho 'something'. 'something to drink'. Chọn D.",
    '144': "Phân tích động từ theo sau: Động từ 'try' mang nghĩa cố gắng làm điều gì đó khó khăn sẽ đi với TO V. 'try TO DO sth'. Ở đây giáo viên 'cố gắng giải thích' (tries to explain). Chọn B.",
    '145': "Phân tích Danh động từ làm chủ ngữ: Giống câu 132, hành động 'Making a lot of money' (Việc kiếm nhiều tiền) đóng vai trò làm chủ ngữ trong câu, nên dùng dạng V-ing đứng đầu câu. Chọn C.",
    '146': "Phân tích động từ theo sau: Động từ 'mind' (phiền lòng, ngại) luôn yêu cầu động từ theo sau ở dạng V-ing. Trong câu đề nghị lịch sự: 'Would you mind DOING sth?' (Bạn có phiền đóng cửa lại không?). Chọn B (closing).",
    '147': "Phân tích từ vựng: Sau mạo từ 'the' cần một danh từ. 'sing' (A) là động từ, 'sang' (B) là V quá khứ, 'singing' (C) là V-ing. 'song' (D) là danh từ (bài hát). 'Bạn có biết bài hát đó không?'. Chọn D.",
    '148': "Phân tích rút gọn mệnh đề quan hệ bị động: Câu đầy đủ 'Many people WHO WERE INVITED couldn\\'t come' (Nhiều người MÀ ĐƯỢC MỜI đã không thể đến). Khi rút gọn bị động, ta chỉ giữ lại P2 'invited'. Chọn D.",
    '149': "Phân tích bị động hiện tại đơn: Chủ ngữ 'English' (Tiếng Anh - vật) không thể tự nói mà 'được nói'. Đây là sự thật hiển nhiên -> bị động hiện tại đơn. 'English' là số ít nên dùng 'is + P2'. 'English is spoken'. Chọn B.",
    '150': "Phân tích giới từ chỉ tác nhân trong câu bị động: Câu bị động 'was arrested' (bị bắt giữ). Để chỉ đối tượng thực hiện hành động bắt giữ (cảnh sát - the police), ta dùng giới từ 'by' (bởi). Chọn B."
}

data['3']['explanations'].update(deep_exp)

with open('reading_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Updated deep explanations for Test 3 (126-150)')
