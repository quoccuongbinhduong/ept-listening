import json

with open('reading_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

deep_exp = {
    '101': "Phân tích giới từ thời gian: Để diễn tả một việc phải hoàn thành 'TRƯỚC' một mốc thời gian trong tương lai (next Thursday), ta dùng giới từ 'by'. Câu mang nghĩa: 'Bạn có thể hoàn thành bài tập trước thứ Năm tuần tới không?'. Chọn B.",
    '102': "Phân tích lượng từ: 'Most' (hầu hết) có thể đi trực tiếp với danh từ số nhiều (Most cars) để chỉ chung chung. Nếu dùng 'Most of' thì bắt buộc phải có mạo từ hoặc tính từ sở hữu (Most of the cars). Trong câu này chỉ nói chung chung 'hầu hết các ô tô ngày nay', ta dùng 'most cars'. Chọn A.",
    '103': "Phân tích từ nhấn mạnh: 'books' là danh từ đếm được số nhiều, vì thế ta dùng 'many' (nhiều). Để nhấn mạnh 'nhiều hơn nữa', ta dùng 'many more' + N (đếm được). (Dùng 'much more' cho N không đếm được). Chọn B.",
    '104': "Phân tích thể giả định (Subjunctive): Trong mệnh đề theo sau các động từ như 'insist' (khăng khăng), 'suggest', 'recommend', động từ luôn chia ở dạng nguyên mẫu không 'to' (V) hoặc phủ định là 'not V' cho mọi ngôi. Ở đây 'smoking indoors NOT BE allowed' là thể giả định. Do đó động từ chính phải là 'insists'. Chọn B.",
    '105': "Phân tích trạng từ nhấn mạnh so sánh hơn: 'harder' là dạng so sánh hơn của tính từ ngắn. Để nhấn mạnh tính từ so sánh hơn (khó hơn NHIỀU), ta dùng 'much'. Cụm: 'much harder to get accustomed to'. Chọn D.",
    '106': "Phân tích sự phối hợp thì: Một hành động đang xảy ra trong quá khứ (chia Quá khứ tiếp diễn) thì có một hành động khác xen vào (chia Quá khứ đơn). Khi anh ấy về nhà (hành động xen vào), vợ anh ấy ĐANG làm bữa tối (was fixing). Chọn D.",
    '107': "Phân tích trạng từ thời gian quá khứ: Cấu trúc 'must have + P2' (chắc hẳn đã) dùng để suy đoán một việc chắc chắn xảy ra trong quá khứ. Vì là quá khứ nên khoảng thời gian (one week) phải đi kèm với 'ago' (cách đây 1 tuần). Chọn B.",
    '108': "Phân tích danh từ chỉ số tiền/mệnh giá: Để nói '200 đô la' (tổng số tiền), ta dùng 'two hundred dollars' (dollar có 's', hundred KHÔNG có 's' vì nó đi sau số đếm 2). Nếu nói 'tờ tiền 200 đô' thì là 'two-hundred-dollar bills' (dollar không 's'). Đáp án chính xác nhất mô tả số tiền là 'two hundred dollars'. Chọn C.",
    '109': "Phân tích phân từ thay thế mệnh đề: Câu đầy đủ 'When it is seen at a distance, it looks like...' (Khi nó ĐƯỢC NHÌN TỪ XA, nó trông như...). Khi rút gọn mệnh đề mang nghĩa bị động, ta giữ lại phân từ 2 (P2). P2 của 'see' là 'Seen'. Chọn A.",
    '110': "Phân tích bị động với động từ khuyết thiếu: 'can' (có thể) đi với câu bị động mang cấu trúc 'can + be + P2'. 'Problem' (vấn đề toán học) phải 'được giải' (be solved). Ghép lại ta có 'can be solved'. Chọn D.",
    '111': "Phân tích từ vựng: 'Although they look alike' (Mặc dù họ trông rất giống nhau) nhưng hai anh em có tính cách 'khác nhau' (different personalities). Chọn A.",
    '112': "Phân tích liên từ tương quan: Đi theo cặp 'neither... nor...' (không... cũng không). Nhân viên mới không tham vọng CŨNG KHÔNG chăm chỉ. Chọn B.",
    '113': "Phân tích liên từ chỉ thời gian: 'He wouldn\\'t leave' (Anh ấy sẽ không rời đi) 'until' (cho đến khi) chuyến tàu của cô ấy khuất bóng. Chọn B.",
    '114': "Phân tích cấu trúc khuyên bảo: 'had better + V' (tốt hơn nên làm gì). Thể phủ định của nó là thêm 'not' đằng sau: 'had better NOT + V' (tốt hơn KHÔNG nên). Chọn D.",
    '115': "Phân tích bị động của động từ giác quan: 'see sb do/doing sth' (nhìn thấy ai làm gì). Khi chuyển sang bị động: 'sb is SEEN DOING sth' (nếu hành động đang diễn ra) hoặc 'sb is SEEN TO DO sth' (nếu hành động trọn vẹn). Ở đây ta có 'was seen washing' (được nhìn thấy đang rửa xe). Chọn A.",
    '116': "Phân tích danh từ không đếm được: 'Information' (thông tin) trong tiếng Anh là danh từ không đếm được, tuyệt đối không bao giờ thêm 's' ở cuối. Để nói 'thêm thông tin', ta dùng 'more information' hoặc 'further information'. Chọn D.",
    '117': "Phân tích đại từ làm tân ngữ của giới từ: Động từ 'carry' mang theo. Để nói 'mang theo bên mình', ta dùng giới từ 'with' + tân ngữ nhân xưng 'you'. Không dùng đại từ phản thân 'yourself' ở đây. 'carry an umbrella with you'. Chọn A.",
    '118': "Phân tích cụm từ cố định: Thành ngữ 'in person' có nghĩa là 'đích thân', 'trực tiếp gặp mặt' (không qua điện thoại hay email). Khách hàng yêu cầu được gặp trực tiếp người quản lý. Chọn C.",
    '119': "Phân tích từ loại: Gia đình đáng kính/được mọi người tôn trọng ta dùng tính từ 'respectable' (đáng kính). 'Respectful' là thể hiện sự tôn trọng với ai đó. 'Respective' là tương ứng. 'Respectable family'. Chọn C.",
    '120': "Phân tích lượng từ: Kính mắt (glasses) có 2 mắt kính (lenses). Do đó để chỉ cả 2 mắt kính đều bị vỡ, ta dùng 'both'. Chọn B.",
    '121': "Phân tích câu bị động quá khứ đơn: Có tác nhân gây ra hành động 'by that terrible wind' (bởi cơn gió khủng khiếp đó) -> câu bị động. Dấu hiệu 'this morning' (sáng nay - thời gian đã qua) -> Quá khứ đơn. Bị động quá khứ đơn 'was/were + P2'. Chọn B (was broken).",
    '122': "Phân tích phủ định của To V: Động từ 'want' đi với 'to V'. Dạng phủ định (không muốn làm gì/muốn KHÔNG làm gì) là thêm 'not' TRƯỚC 'to V' -> 'not to fail'. Anh ấy muốn không bị trượt kỳ thi. Chọn B.",
    '123': "Phân tích liên từ chỉ nguyên nhân: Hai mệnh đề là 'nghiên cứu phát hiện ra vấn đề' và 'công ty quyết định dừng dự án'. Đây là quan hệ Nguyên nhân - Kết quả. Từ mang nghĩa 'Vì' là 'Since' (tương đương Because). Chọn A.",
    '124': "Phân tích từ vựng: 'The deadline' (hạn chót) vẫn chưa được quyết định. Các từ khác không hợp nghĩa. Chọn A.",
    '125': "Phân tích câu điều kiện loại 3 ẩn ý: Cụm 'With only one more week' tương đương với mệnh đề điều kiện 'If he had had one more week' (Nếu anh ấy có thêm 1 tuần nữa trong quá khứ). Do đó mệnh đề chính chia theo câu điều kiện loại 3: 'could have + P2' (could have been). Chọn A."
}

data['4']['explanations'].update(deep_exp)

with open('reading_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Updated deep explanations for Test 4 (101-125)')
