import json

with open('reading_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

exp = {
    '114': 'Cấu trúc "tell someone to do something" (bảo ai đó làm gì).',
    '115': 'Cấu trúc "It is + adj + to do something" (Thật là ... để làm gì).',
    '116': 'Cấu trúc "have time to do something" (có thời gian để làm gì).',
    '117': 'Lend: cho mượn. (Borrow: mượn). "Could you lend me" = "Bạn có thể cho tôi mượn".',
    '118': "Chủ ngữ 'they' (số nhiều) ở hiện tại đơn dùng trợ động từ 'don\\'t'.",
    '119': '"People" là danh từ số nhiều. Trong các đáp án chỉ có "were" là động từ to be chia ở số nhiều (quá khứ).',
    '120': 'Đi bằng phương tiện gì dùng giới từ "by" (by train: bằng tàu hỏa).',
    '121': 'Cấu trúc "had better + V (nguyên mẫu)" (tốt hơn hết nên làm gì).',
    '122': 'Bring: mang đến. "Bring me" (Mang cho tôi).',
    '123': 'Thì hiện tại hoàn thành, "already" (đã rồi) đứng giữa trợ động từ "have" và động từ chính phân từ 2.',
    '124': '"in + khoảng thời gian" dùng trong thì tương lai mang nghĩa "trong bao lâu nữa" (in a few minutes).',
    '125': '"by + thời gian" mang nghĩa là trước lúc đó (trước 6 giờ).',
    '126': 'Mệnh đề quan hệ, giới từ "to" (trong speak to) đảo lên trước đại từ quan hệ "whom".',
    '127': '"open" ở đây đóng vai trò là tính từ (mở cửa).',
    '128': 'Sau động từ to be "is" cần một tính từ. "patient" (kiên nhẫn) là tính từ.',
    '129': 'Dựa vào nghĩa: Không ai trong số họ biết nấu ăn, vì vậy họ THƯỜNG (often) đi ăn ngoài.',
    '130': 'Cấu trúc "go to + địa điểm" (đi đến đâu).',
    '131': 'So sánh hơn với tính từ dài (expensive) dùng "more + adj".',
    '132': 'Để nhấn mạnh so sánh hơn, ta dùng "much" đứng trước (much more attractive).',
    '133': 'There are no + danh từ (Không có...). Không dùng "not" vì không có mạo từ/lượng từ.',
    '134': 'The date (ngày) đi với giới từ "on", đại từ quan hệ thay thế là "which" -> "on which".',
    '135': 'So sánh hơn của "little" (dùng cho danh từ không đếm được như money) là "less".',
    '136': 'Thành ngữ "on time" nghĩa là đúng giờ.',
    '137': 'Liên từ "As soon as" nghĩa là "Ngay khi".',
    '138': 'Câu điều kiện loại 2, mệnh đề If chia ở quá khứ đơn (could).',
    '139': 'Cấu trúc "so + adj + that" (quá ... đến nỗi mà).',
    '140': 'Cấu trúc "interested in" (thích thú với). So sánh hơn dùng "more interested".',
    '141': 'Trong câu hỏi mang tính chất xin phép, yêu cầu lịch sự, ta dùng "some".',
    '142': 'Đi bằng phương tiện giao thông dùng giới từ "by" (by bus).',
    '143': 'Hiện tại phân từ (V-ing) đứng đầu câu làm trạng ngữ chỉ nguyên nhân. Phủ định thêm "Not" ở trước (Not wearing).',
    '144': "Trong câu phủ định (don't have) ta dùng 'any'.",
    '145': 'Dùng tính từ đuôi "-ing" (interesting) để chỉ tính chất của sự vật (bộ phim).',
    '146': 'Cấu trúc "hope + to V" (hi vọng làm gì).',
    '147': 'Giới từ "on" dùng cho bề mặt (on the top shelf - trên kệ).',
    '148': 'Cấu trúc "make a mistake" (phạm sai lầm). Quá khứ là "made".',
    '149': 'Từ chỉ màu sắc trong các đáp án là "orange" (màu cam).',
    '150': '"students" là danh từ đếm được số nhiều, nên dùng "a few" (một vài).'
}

trans = {
    '114': 'Sếp bảo tôi phải hoàn thành dự án trước thứ Sáu này.',
    '115': 'Thật khó để chèo thuyền từ Anh sang Pháp.',
    '116': 'Tôi không có thời gian để tìm chiếc xe rẻ nhất.',
    '117': 'Trời đang mưa. Bạn có thể cho tôi mượn ô không?',
    '118': 'Vào ban ngày, họ không có thời gian để hoàn thành công việc.',
    '119': 'Tất cả mọi người ở đó đều đến từ Nhật Bản.',
    '120': 'Tôi đã đi đến thành phố bằng tàu hỏa.',
    '121': 'Tôi tốt hơn là nên đi ngủ bây giờ để sáng mai dậy sớm.',
    '122': 'Bạn có thể mang cho tôi chiếc áo len màu đỏ được không?',
    '123': 'Chúng tôi đã giải quyết xong vấn đề rồi.',
    '124': 'Chúng ta sẽ đến đó trong vài phút nữa.',
    '125': 'Sáng mai, bạn phải thức dậy trước 6 giờ.',
    '126': 'Người đàn ông mà Linda đã nói chuyện cùng là giáo viên tiếng Anh của cô ấy.',
    '127': 'Cửa hàng có mở cửa vào Chủ nhật không?',
    '128': 'Anh ấy luôn luôn rất kiên nhẫn.',
    '129': 'Không ai trong số họ biết nấu ăn, vì vậy họ thường đi ăn ngoài.',
    '130': 'Họ đã đi Guam vào kỳ nghỉ.',
    '131': 'Cái này đắt hơn cái kia.',
    '132': 'Chiếc ví màu đen này hấp dẫn hơn nhiều so với chiếc màu nâu.',
    '133': 'Không có công nhân nào đang hái bông trên cánh đồng.',
    '134': 'Ngày 31 tháng 12 là ngày mà chúng ta gặp nhau mỗi năm.',
    '135': 'Bây giờ tôi có ít tiền hơn năm ngoái.',
    '136': 'Gary lại đến muộn. Anh ấy chưa bao giờ đúng giờ!',
    '137': 'Ngay khi bạn nghe thấy tiếng chuông, bạn cần phải rời khỏi lớp học.',
    '138': 'Nếu tôi có thể giúp bạn, tôi sẽ làm.',
    '139': 'Cô ấy quá thông minh đến nỗi đã đạt điểm cao nhất trong bài kiểm tra.',
    '140': 'Anh ấy quan tâm đến tiền bạc nhiều hơn anh trai mình.',
    '141': 'Tôi có thể mượn một ít tiền được không?',
    '142': 'Hôm qua, tôi đi học bằng xe buýt.',
    '143': 'Vì không thắt cà vạt, anh ấy không thể vào nhà hàng.',
    '144': 'Tôi không có đồng tiền nào cả.',
    '145': 'Bộ phim đó rất thú vị.',
    '146': 'Họ hi vọng sẽ đi du lịch Singapore vào năm tới.',
    '147': 'Hãy đặt sữa ở kệ trên cùng của tủ lạnh.',
    '148': 'Ôi! Tôi đã mắc sai lầm!',
    '149': 'Màu sắc yêu thích của tôi là màu cam.',
    '150': 'Có một vài học sinh đang đợi giáo viên của họ.'
}

data['1']['explanations'].update(exp)
data['1']['translations'].update(trans)

with open('reading_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Updated 114-150')
