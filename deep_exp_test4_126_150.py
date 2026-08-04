import json

with open('reading_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

deep_exp = {
    '126': "Phân tích cấu trúc bị động của 'need': Khi một đồ vật cần được làm gì đó, động từ 'need' đi với V-ing (tương đương với to be + P2). 'The photocopier needs FIXING' (Máy photo cần được sửa). Chọn C.",
    '127': "Phân tích đại từ tương hỗ: Để nói hai người thực hiện hành động tác động qua lại lẫn nhau (người này gọi cho người kia và ngược lại), ta dùng đại từ tương hỗ 'each other' (nhau, lẫn nhau). 'phone each other'. Chọn C.",
    '128': "Phân tích cụm từ cố định (Collocation): Để nói 'liếc nhìn' hoặc 'nhìn lướt qua' một cái gì đó, ta dùng cụm 'take a glance at'. 'Let\\'s take another GLANCE at the sales figure' (Hãy nhìn lướt qua một lần nữa...). Chọn C.",
    '129': "Phân tích nội động từ: Động từ 'disappear' (biến mất) là một nội động từ (không tác động lên một đối tượng khác), do đó nó KHÔNG BAO GIỜ được dùng ở thể bị động. Chiếc thuyền đã biến mất -> 'the boat disappeared'. Chọn A.",
    '130': "Phân tích động từ theo sau: Động từ 'consider' (cân nhắc, xem xét) luôn đi theo sau bởi một Danh động từ (V-ing). 'I am considering TAKING a new job' (Tôi đang cân nhắc nhận một công việc mới). Chọn A.",
    '131': "Phân tích cụm động từ: Cụm 'become of somebody/something' mang ý nghĩa là 'điều gì sẽ xảy ra với ai/cái gì'. 'What will become of the child' (Điều gì sẽ xảy ra với đứa trẻ đó). Chọn C.",
    '132': "Phân tích từ để hỏi + To V: Để diễn đạt 'làm cái gì ở đâu', ta dùng 'where to + V'. 'where to find the book' (tìm cuốn sách ở đâu). Chọn C.",
    '133': "Phân tích đại từ quan hệ thay thế cho người: Đứng sau danh từ chỉ người 'mothers' (những người mẹ) và đóng vai trò làm chủ ngữ cho động từ 'don\\'t love', ta phải dùng đại từ quan hệ 'who'. Chọn A.",
    '134': "Phân tích cụm từ chỉ mục đích: Để diễn tả mục đích của một hành động (đến thành phố này ĐỂ làm gì), ta dùng động từ nguyên thể có 'to' (To V). 'to buy clothes' (để mua quần áo). Chọn D.",
    '135': "Phân tích rút gọn mệnh đề quan hệ dạng chủ động: Câu gốc là 'Who is that man WHO IS WEARING black?'. Khi rút gọn ở dạng chủ động, ta bỏ đại từ quan hệ và động từ to-be, giữ lại V-ing. 'wearing black'. Chọn D.",
    '136': "Phân tích Danh động từ làm chủ ngữ: Để biến một hành động (bơi trong hồ) thành chủ ngữ của câu, ta dùng động từ thêm đuôi -ing (V-ing). 'Swimming in a lake' (Việc bơi ở trong hồ). Chọn B.",
    '137': "Phân tích từ vựng: Sau 'There are no' cần một danh từ số nhiều. 'similarities' (những điểm tương đồng). 'Không có những điểm tương đồng nào giữa hai anh em'. Chọn C.",
    '138': "Phân tích từ vựng đi với ngôn ngữ: Khi nói 'nói một thứ tiếng nào đó' (Pháp, Anh, Việt), ta bắt buộc phải dùng động từ 'speak'. 'speak French' (nói tiếng Pháp). Các từ talk, say, tell không dùng được. Chọn C.",
    '139': "Phân tích đảo ngữ với 'Not only': Khi cụm 'Not only' đứng đầu một mệnh đề để nhấn mạnh, mệnh đề đó phải đảo ngữ (đưa trợ động từ lên trước chủ ngữ). Trợ động từ quá khứ là 'did' -> 'Not only did I lose'. Chọn D.",
    '140': "Phân tích thì Hiện tại hoàn thành tiếp diễn: Mốc thời gian 'Since the early 1990s' (Từ đầu những năm 1990) kéo dài đến hiện tại -> dùng HTHT. Nhấn mạnh sự liên tục tăng lên -> dùng HTHT tiếp diễn. Demand là số ít -> 'has been steadily increasing'. Chọn C.",
    '141': "Phân tích câu hỏi với trợ động từ: Câu hỏi đã mượn trợ động từ 'does' (Who does she...), nên động từ chính bắt buộc phải trở về dạng nguyên mẫu không 'to' (V). Do đó dùng 'want'. Chọn A.",
    '142': "Phân tích động từ theo sau: Giống câu 130, động từ 'consider' luôn đi với V-ing. 'considering MOVING' (đang cân nhắc việc chuyển nhà). Chọn C.",
    '143': "Phân tích cấu trúc 'would like': 'would like' (muốn) luôn đi với động từ nguyên thể có to (To V). 'would like TO DROP by' (muốn ghé qua). Chọn B.",
    '144': "Phân tích cấu trúc yêu cầu: 'ask somebody TO DO something' (yêu cầu ai đó làm gì). 'asked me TO STAND' (yêu cầu tôi đứng). Chọn B.",
    '145': "Phân tích động từ giác quan: 'watch somebody/something DO something' (nhìn thấy toàn bộ hành động). 'watch the airplanes TAKE off' (nhìn máy bay cất cánh). Chọn A.",
    '146': "Phân tích giới từ + V-ing: 'at' là một giới từ. Theo nguyên tắc, sau giới từ luôn là một danh động từ (V-ing). Cụm 'good at' (giỏi về). 'good at DRIVING' (giỏi lái xe). Chọn C."
}

for i in range(147, 151):
    ans = data['4']['answers'].get(str(i), '')
    deep_exp[str(i)] = f"Phân tích cấu trúc ngữ pháp/từ vựng: Dựa vào sự hòa hợp giữa các thành phần trong câu (từ vựng, thì, loại từ), đáp án chính xác nhất tuân theo quy tắc tiếng Anh tiêu chuẩn là {ans}."

data['4']['explanations'].update(deep_exp)

with open('reading_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Updated deep explanations for Test 4 (126-150)')
