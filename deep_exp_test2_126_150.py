import json

with open('reading_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

deep_exp = {
    '126': "Phân tích giới từ đi kèm động từ: Cụm động từ (Phrasal verb) 'turn into' có nghĩa là 'biến thành' hoặc 'chuyển sang' trạng thái khác. Cuộc thảo luận của chúng tôi đã chuyển thành một cuộc cãi vã lớn (turned into a big fight). Do đó chọn B.",
    '127': "Phân tích cấu trúc chủ ngữ giả: Cấu trúc: 'It is + tính từ + FOR somebody + TO DO something' (Thật là ... cho ai đó để làm việc gì). Trong câu này: It's impossible (Thật là không thể) + FOR a penguin (cho một con chim cánh cụt) + to fly (có thể bay). Chọn C (for).",
    '128': "Phân tích đại từ quan hệ chỉ sự sở hữu: Danh từ đứng trước là 'the house' (ngôi nhà), danh từ đứng sau là 'roof' (mái nhà). Mối quan hệ ở đây là 'mái của ngôi nhà đó' (sở hữu cách). Đại từ quan hệ chỉ sở hữu duy nhất trong tiếng Anh là 'whose'. Chọn D.",
    '129': "Phân tích giới từ thời gian: 'twenty years' (20 năm) là một KHOẢNG thời gian. Trong thì hiện tại hoàn thành / hiện tại hoàn thành tiếp diễn, để diễn đạt hành động kéo dài trong một khoảng thời gian, ta dùng giới từ 'for'. Chọn C.",
    '130': "Phân tích cấu trúc danh từ + động từ nguyên thể: 'time' (thời gian) khi muốn nói 'thời gian để làm gì' thì động từ theo sau phải ở dạng TO V. 'enough time TO wait for you' (đủ thời gian ĐỂ đợi bạn). Chọn B.",
    '131': "Phân tích giới từ chỉ thời gian: Câu sử dụng thì hiện tại hoàn thành tiếp diễn (have been learning). Đằng sau là 'three years' (3 năm). Thông thường ta dùng 'for three years'. Tuy nhiên trong các đáp án không có 'for', ta dùng 'over' mang nghĩa 'hơn' (hơn 3 năm). Chọn B.",
    '132': "Phân tích giới từ chỉ giờ giấc: Đứng trước một mốc thời gian cụ thể trong ngày (giờ) như 'seven o\\'clock' (7 giờ), bắt buộc phải dùng giới từ 'at'. Chọn B.",
    '133': "Phân tích sự hòa hợp Chủ ngữ - Động từ: Chủ ngữ gồm 2 thành phần nối với nhau bằng cụm 'as well as' (cũng như): S1 (The students) as well as S2 (the teacher). Theo quy tắc ngữ pháp, động từ phải chia theo Chủ ngữ 1 (S1). S1 ở đây là 'The students' (số nhiều), do đó động từ to-be phải là số nhiều trong quá khứ 'were'. Chọn D.",
    '134': "Phân tích chủ ngữ tập hợp: Động từ trong câu là 'are' (số nhiều). Ta áp dụng quy tắc: 'A number of + N số nhiều' đi với động từ chia SỐ NHIỀU. 'The number of + N số nhiều' đi với động từ chia SỐ ÍT. Do câu dùng 'are' nên ta phải chọn 'A number of' (Một lượng lớn...). Chọn A.",
    '135': "Phân tích cấu trúc khuyên bảo/yêu cầu: Trong các đáp án, chỉ có động từ 'tell' (quá khứ là told) mới đi liền với một tân ngữ (you) và TO V (to do) mang nghĩa yêu cầu ai làm gì. Cấu trúc 'tell somebody to do something' (Bảo ai làm gì). Chọn C.",
    '136': "Phân tích thì của câu: Từ khóa 'already' (đã... rồi) là dấu hiệu nhận biết của thì Hiện tại hoàn thành, diễn tả một hành động đã hoàn tất trước hiện tại. Cấu trúc: 'have/has + P2'. Do đó chọn B (have read).",
    '137': "Phân tích sự phối hợp thì: Câu có 2 hành động trong quá khứ. Hành động 'he told me' (anh ấy kể cho tôi nghe) chia ở quá khứ đơn. Hành động 'nghe về câu chuyện vui' xảy ra TRƯỚC khi anh ấy kể, do đó phải chia ở thì Quá khứ hoàn thành (had + P2). Chọn C (had heard).",
    '138': "Phân tích câu gián tiếp: Câu trực tiếp là 'I have already finished my project' (Hiện tại hoàn thành). Khi tường thuật lại qua động từ 'told', ta phải LÙI THÌ từ Hiện tại hoàn thành xuống Quá khứ hoàn thành (had + P2). Do đó 'have already finished' lùi thành 'had already finished'. Chọn A.",
    '139': "Phân tích danh từ không đếm được: 'All of the food' (Tất cả thức ăn). Danh từ 'food' là danh từ không đếm được, luôn chia động từ ở số ít. Câu mang ý nghĩa bị động trong quá khứ (được chuẩn bị xong trước 7 giờ). Động từ to-be số ít trong quá khứ là 'was'. Chọn A.",
    '140': "Phân tích cấu trúc 'would rather': Cấu trúc 'would rather' (thích/muốn... hơn) đi với động từ nguyên mẫu không to (V). Khi muốn phủ định, ta thêm 'not' ngay sau 'rather'. Cấu trúc: 'would rather NOT V'. Chọn D (rather not go).",
    '141': "Phân tích cấu trúc 'would like': 'Would like' mang ý nghĩa mời mọc, đề nghị lịch sự. Nó luôn đi kèm với TO V. 'Would you like TO GO SHOPPING with me?' (Bạn có muốn đi mua sắm cùng tôi không?). Chọn B.",
    '142': "Phân tích trạng từ chỉ tần suất: 'always' (luôn luôn) là dấu hiệu của thì Hiện tại đơn, diễn tả một thói quen. Chủ ngữ là 'They' (số nhiều) nên động từ 'try' giữ nguyên. Cụm 'try on' nghĩa là thử đồ/giày dép. Chọn A (try on).",
    '143': "Phân tích sự phối hợp thì quá khứ: Cấu trúc hành động đang xảy ra (chia Quá khứ tiếp diễn) thì có hành động khác xen vào (chia Quá khứ đơn). Tên trộm 'đang đếm tiền' (was counting) thì cảnh sát 'đến' (arrived). Chủ ngữ 'The robber' số ít nên dùng 'was'. Chọn B.",
    '144': "Phân tích cấu trúc 'đã từng': Cấu trúc 'used to + V (nguyên mẫu)' mang ý nghĩa mô tả một thói quen hoặc trạng thái đã từng xảy ra trong quá khứ nhưng hiện tại không còn nữa. 'Vợ tôi đã từng làm việc ở công ty GoodAll'. Chọn B.",
    '145': "Phân tích cấu trúc 'would like': Cấu trúc 'would like SOMEBODY to do something' (muốn ai đó làm gì cho mình một cách lịch sự). 'Người quản lý muốn chúng tôi trả lại đĩa DVD trước buổi trưa nay'. Chọn A (would like).",
    '146': "Phân tích cụm từ đi liền (collocation): 'go' đi với các hoạt động giải trí kết thúc bằng -ing. Ví dụ: go fishing (đi câu cá), go swimming (đi bơi), go shopping (đi mua sắm). Do đó chọn A.",
    '147': "Phân tích từ vựng nghề nghiệp: Chủ ngữ 'I' đã làm việc cho ai đó. Chỗ trống cần một danh từ chỉ người. 'Employer' là ông chủ, người thuê lao động. 'Employee' là nhân viên. 'Tôi đã làm việc cho ông chủ của tôi được 2 năm'. Chọn C.",
    '148': "Phân tích giới từ chỉ địa điểm: Để chỉ một địa điểm chung chung mang tính chất tổ chức (trường học, bệnh viện, nhà ga), ta dùng giới từ 'at'. 'eat lunch at school' (ăn trưa ở trường). Chọn A.",
    '149': "Phân tích cấu trúc 'have been to': Cấu trúc 'have/has been to + địa điểm' có nghĩa là 'đã từng đi đến đó (và đã trở về)'. 'Chúng tôi đã đi London 3 lần'. Chọn D (been). Không dùng 'gone to' vì nó có nghĩa là đã đi nhưng chưa về.",
    '150': "Phân tích thì Hiện tại hoàn thành tiếp diễn: Mệnh đề chứa 'since' (từ khi) đi với quá khứ đơn (I came in). Mệnh đề chính chia ở Hiện tại hoàn thành hoặc Hiện tại hoàn thành tiếp diễn để nhấn mạnh quá trình liên tục. 'Cô ấy đã và đang nói chuyện điện thoại kể từ lúc tôi bước vào'. Chọn C (has been talking)."
}

data['2']['explanations'].update(deep_exp)

with open('reading_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Updated deep explanations for Test 2 (126-150)')
