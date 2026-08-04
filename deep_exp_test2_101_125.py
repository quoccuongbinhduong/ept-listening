import json

with open('reading_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

deep_exp = {
    '101': "Phân tích thì và động từ: Chủ ngữ là 'I' (ngôi thứ nhất số ít). Ở thì hiện tại đơn mang ý nghĩa sở hữu, ta dùng động từ 'have' (có). Động từ 'has' chỉ dùng cho chủ ngữ ngôi thứ 3 số ít (He, she, it). 'Do' và 'does' là trợ động từ, không mang nghĩa 'có'. Vì thế đáp án đúng là D (have).",
    '102': "Phân tích cấu trúc nghi vấn hiện tại đơn: Chủ ngữ là 'you' và động từ thường là 'like'. Để tạo câu hỏi với động từ thường ở hiện tại đơn, ta phải mượn trợ động từ 'Do' đảo lên trước chủ ngữ. Cấu trúc: Do + S + V(nguyên mẫu)? Vì vậy chọn C (Do). Không dùng 'Are' vì 'Are' là động từ to-be không đi kèm với động từ thường nguyên mẫu 'like'.",
    '103': "Phân tích cấu trúc nghi vấn Wh-question: Câu hỏi 'Where ... he work?'. Chủ ngữ là 'he' (ngôi thứ 3 số ít), động từ chính là 'work' (động từ thường). Trợ động từ tương ứng phải là 'does'. Cấu trúc: Wh- + do/does + S + V? Do đó chọn C (does).",
    '104': "Phân tích thì tương lai đơn: Câu hỏi có 'will' (sẽ) - trợ động từ thì tương lai đơn. Theo sau 'will' luôn là một động từ nguyên thể không chia. Trong 4 đáp án: A (do) là nguyên thể, B (doing) là V-ing, C (did) là quá khứ, D (done) là phân từ 2. Do đó chọn A.",
    '105': "Phân tích giới từ chỉ nghề nghiệp: Khi muốn nói ai đó làm việc 'với tư cách là' hoặc 'như là' một nghề gì, ta dùng giới từ 'as'. Cấu trúc: 'work as a/an + nghề nghiệp'. Do đó, 'works as a doctor' (làm bác sĩ) là chính xác. Chọn C.",
    '106': "Phân tích từ vựng đặc biệt: 'Broke' (A) khi là tính từ mang nghĩa lóng là 'cháy túi', 'hết tiền' hoặc 'phá sản'. Câu trước là 'I have no money' (Tôi không có tiền) thì câu sau mô tả trạng thái 'I am broke' (Tôi viêm màng túi rồi) là hoàn toàn hợp lý. Các từ broken, breaking, break không mang nghĩa này. Chọn D.",
    '107': "Phân tích lượng từ: Đằng sau có 'my friends' (danh từ đếm được số nhiều có tính từ sở hữu 'my'). Ta không dùng 'Many my friends' mà bắt buộc phải có giới từ 'of' chen giữa lượng từ và tính từ sở hữu. Cấu trúc: 'Many of + the/my/his... + danh từ số nhiều'. Do đó chọn D (Many of).",
    '108': "Phân tích lượng từ: 'Students' là danh từ đếm được số nhiều đứng ngay sau chỗ trống (không có the hay tính từ sở hữu). Ta dùng trực tiếp 'Most' (Hầu hết) + N số nhiều. 'Almost' là trạng từ, không đứng trực tiếp trước N. 'Much' dùng cho N không đếm được. 'Each' dùng cho N số ít. Do đó chọn A.",
    '109': "Phân tích cấu trúc động từ 'seem': Động từ 'seem' (có vẻ như) luôn đi với động từ nguyên mẫu có 'to'. Cấu trúc: 'seem TO DO something'. Ở đây là 'seem to enjoy'. Do đó chọn A.",
    '110': "Phân tích cấu trúc kết quả: Cấu trúc 'so + tính từ/trạng từ + that...' (quá... đến nỗi mà). 'He wandered so far that...' (Anh ấy đi lang thang quá xa đến nỗi mà...). Các từ very, such, really không tạo thành cấu trúc đi liền với 'that' trong trường hợp này. Chọn A.",
    '111': "Phân tích từ vựng: 'explode' (động từ) nghĩa là nổ tung, phát nổ. 'explore' (động từ) nghĩa là khám phá. Tàu (the ship) bị phát nổ (exploded) thì nhiều người mới thiệt mạng. Chọn B.",
    '112': "Phân tích mệnh đề quan hệ: Danh từ đứng trước là 'the sport' (môn thể thao - chỉ vật). Đại từ quan hệ thay thế cho vật, đóng vai trò tân ngữ (môn mà tôi thích nhất) là 'which'. 'Who/whom' dùng cho người, 'whose' dùng cho sở hữu. Chọn C.",
    '113': "Phân tích mệnh đề quan hệ chỉ nơi chốn: Danh từ 'The hotel' chỉ địa điểm. Động từ trong mệnh đề là 'stayed'. Ta nói 'stay at the hotel' (ở tại khách sạn). Khi đảo thành mệnh đề quan hệ, giới từ 'at' được đưa lên trước đại từ quan hệ 'which' -> 'at which'. Chọn D.",
    '114': "Phân tích so sánh hơn nhấn mạnh: Tính từ 'deep' (sâu) là tính từ ngắn, dạng so sánh hơn là 'deeper'. Để nhấn mạnh sự so sánh hơn (sâu hơn NHIỀU), ta dùng 'much' đứng trước dạng so sánh hơn -> 'much deeper'. Do đó chọn B.",
    '115': "Phân tích so sánh nhất: Có mạo từ 'the' đứng trước chỗ trống và phạm vi 'in the museum' (trong bảo tàng). Đây là so sánh nhất. 'Interesting' là tính từ dài, nên dùng 'most interesting'. Chọn D.",
    '116': "Phân tích so sánh hơn của trạng từ: 'Quickly' là trạng từ bổ nghĩa cho động từ 'run'. So sánh hơn của trạng từ dài dùng 'more quickly'. Chủ ngữ 'Sally' (ngôi thứ 3 số ít) nên động từ 'run' phải thêm 's' -> 'runs'. Ghép lại ta có 'runs more quickly'. Chọn C.",
    '117': "Phân tích trạng từ thời gian: Thì của câu là Hiện tại hoàn thành (have been). Trong các đáp án, chỉ có 'lately' (gần đây, mới đây) là trạng từ thời gian thường được dùng với thì hiện tại hoàn thành. Chọn B.",
    '118': "Phân tích liên từ: Mệnh đề 1: 'Her skin would not burn' (Da cô ấy sẽ không bị cháy). Mệnh đề 2: 'she wore sunscreen' (cô ấy bôi kem chống nắng). Mối quan hệ nguyên nhân - kết quả: Da không cháy VÌ bôi kem. Liên từ chỉ nguyên nhân là 'because'. Chọn A.",
    '119': "Phân tích cấu trúc 'give': Động từ 'give' (tặng, đưa) có 2 cấu trúc: 1. give sb sth. 2. give sth TO sb. Ở đây là 'give a thank-you card TO our teacher'. Do đó chọn C.",
    '120': "Phân tích giới từ chỉ mục đích: 'For' có nghĩa là 'cho', 'dành cho'. Mẹ tôi mua một chiếc điện thoại DÀNH CHO (hoặc LÀM) món quà sinh nhật của tôi. Chọn B.",
    '121': "Phân tích thể bị động trong quá khứ: Chủ ngữ mệnh đề sau là 'the school' (ngôi trường), hành động là 'build' (xây dựng). Trường học phải được xây dựng (bị động). Thời gian 'in 1946' là mốc quá khứ. Bị động quá khứ đơn: 'was/were + P2'. Do đó chọn 'was built' (A).",
    '122': "Phân tích giới từ chỉ khoảng thời gian: 'During + danh từ' có nghĩa là trong suốt khoảng thời gian diễn ra sự kiện đó. 'During the soccer match' (trong lúc diễn ra trận bóng). 'By' là trước, 'over' là vượt qua. Chọn B.",
    '123': "Phân tích cấu trúc 'buy': Tương tự 'give', động từ 'buy' (mua) có cấu trúc: buy sb sth HOẶC buy sth FOR sb (mua cái gì cho ai). Chọn A.",
    '124': "Phân tích dạng phủ định của V-ing/to V: Động từ 'prefer' có thể đi với V-ing (thích làm gì hơn). Dạng phủ định của V-ing là đặt 'not' trước V-ing -> 'not walking'. Nghĩa: Họ không thích đi bộ qua đường phố vào ban đêm. Chọn B.",
    '125': "Phân tích từ hạn định: 'Pens' (những chiếc bút khác) là danh từ số nhiều. 'Another' (một cái khác) cộng với danh từ số ít. 'Other' + danh từ số nhiều (những cái khác). Ở đây câu hỏi có 'pens' (số nhiều) nên dùng 'other pens'. Chọn A."
}

data['2']['explanations'].update(deep_exp)

with open('reading_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Updated deep explanations for Test 2 (101-125)')
