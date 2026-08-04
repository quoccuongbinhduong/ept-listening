import json

with open('reading_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

deep_exp = {
    '151': "Chi tiết biểu đồ: Mặc dù OCR không quét được cột tháng 1, nhưng dựa vào đồ thị cột trong bài thi gốc, số lượng kem bán ra trong tháng 1 (January) là 90 lít.",
    '152': "Chi tiết biểu đồ: Tháng có cột đồ thị thấp nhất là tháng 2 (February). Do đó Ike bán được ít kem nhất vào tháng 2.",
    '153': "Chi tiết biểu đồ: Biểu đồ thống kê số liệu trong 6 tháng (Jan, Feb, Mar, Apr, May, Jun). Quãng thời gian 6 tháng tương đương với nửa năm (Half a year).",
    '154': "Chi tiết trong bài: Brenda ghi lại lời nhắn: 'He asked me to tell you to make sure to pick him up at 6 o\\'clock at the North York branch office' (anh ấy bảo đón ở văn phòng chi nhánh North York). Tức là yêu cầu đón ở một địa điểm khác (another location).",
    '155': "Chi tiết trong bài: 'he will be spending his day there to attend a meeting' (anh ấy sẽ dành thời gian ở đó để tham dự một cuộc họp). Tức là anh ấy họp trước khi đến hội thảo.",
    '156': "Chi tiết trong bài: Thư viện đóng cửa 'December 24-25 and December 31-January 1'. Ngày 26/12 (December 26th) không nằm trong danh sách ngày nghỉ, do đó thư viện vẫn mở cửa.",
    '157': "Chi tiết trong bài: Dòng thông báo 'Because of the Christmas and New Year holidays, the library will be closed...' (Vì kỳ nghỉ lễ Giáng Sinh và Năm Mới, thư viện sẽ đóng cửa...).",
    '158': "Chi tiết trong bài: 'Regular bus fares will rise 15%' (Giá vé xe buýt thông thường sẽ tăng 15%).",
    '159': "Chi tiết trong bài: Câu cuối của thông báo ghi 'The increase is scheduled to go into effect next month' (Việc tăng giá dự kiến sẽ có hiệu lực vào tháng tới).",
    '160': "Chi tiết trong bài: Lá thư mở đầu bằng 'we are concerned that our employees are arriving late for work' (chúng tôi lo ngại rằng nhân viên của chúng tôi đang đến chỗ làm muộn).",
    '161': "Chi tiết trong bài: Người viết đề xuất: 'We wonder if it would be possible to have the morning bus depart 15 minutes earlier' (Chúng tôi tự hỏi liệu chuyến xe buýt buổi sáng có thể khởi hành sớm hơn 15 phút không). Tức là muốn thay đổi/sửa lại lịch trình xe buýt (Revise the buses schedule).",
    '162': "Chi tiết trong bài: Tại hội chợ việc làm, bạn có cơ hội 'meet people who are currently working in these... fields and who have job openings for you' (gặp gỡ những người... có vị trí việc làm trống cho bạn). Đó chính là những nhà tuyển dụng tiềm năng (potential employers).",
    '163': "Chi tiết trong bài: Câu đầu tiên 'A job fair will be held at the Downtown Convention Center' (Một hội chợ việc làm sẽ được tổ chức tại Trung tâm Hội nghị Downtown).",
    '164': "Suy luận từ bài đọc: Dòng 'Please examine the contents of this package immediately' (Vui lòng kiểm tra các món đồ trong kiện hàng này ngay lập tức). Điều này chứng tỏ tờ hướng dẫn này được đính kèm bên trong kiện hàng (Enclosed in a package).",
    '165': "Phân tích từ vựng: Từ 'condition' trong cụm 'undamaged condition' (tình trạng không bị hư hại) đồng nghĩa với 'state' (trạng thái, tình trạng).",
    '166': "Chi tiết trong bài: Hướng dẫn đổi trả ghi: 'repack it in the same box... apply the enclosed return shipping label... and return postage will be paid by the customer' (đóng gói lại vào hộp cũ, dán nhãn vận chuyển... khách hàng tự trả phí bưu điện). Tức là đóng gói và gửi qua đường bưu điện (Repack it and mail it back).",
    '167': "Chi tiết trong bài: 'return it to us within thirty days for a full refund, no questions asked' (trả lại trong vòng 30 ngày để được hoàn tiền ĐẦY ĐỦ, không cần hỏi thêm). Bạn sẽ nhận lại toàn bộ số tiền (get all your money back).",
    '168': "Chi tiết trong bài: 'the two left lanes on the north side will be closed' (hai làn bên trái ở phía bắc sẽ bị đóng).",
    '169': "Chi tiết trong bài: Thông báo được phát đi bởi 'Miami-Dade COUNTY Transit Authority' (Cơ quan Vận tải QUẬN/HẠT Miami-Dade). Do đó cấp quản lý là County.",
    '170': "Chi tiết trong bài: Việc phong tỏa kéo dài từ đường 'NE 79th St. to NE 135th St.'. Lối ra NE 151st Street nằm ngoài khoảng này, do đó sẽ KHÔNG bị ảnh hưởng.",
    '171': "Chi tiết hóa đơn: Tổng hóa đơn = $1500 + $125 + $750 = $2375.",
    '172': "Chi tiết trong bài: Hóa đơn ghi ngày May 30. Điều khoản ghi: 'payable in full within fifteen days of the date of this invoice' (thanh toán đủ trong vòng 15 ngày kể từ ngày hóa đơn). 15 ngày sau 30/5 là khoảng giữa tháng 6 (June 15).",
    '173': "Chi tiết trong bài: Thông báo có nhắc đến 'total relaxation' (thư giãn hoàn toàn), 'full bodywork' (chăm sóc toàn thân), 'neck, shoulders, and back' (cổ, vai, lưng). Đây là dịch vụ mát-xa (Massages).",
    '174': "Chi tiết trong bài: Có dòng 'free of charge' (hoàn toàn miễn phí). Do đó nhân viên không phải trả tiền (They pay nothing).",
    '175': "Chi tiết trong bài: Oscar gửi fax để 'faxing you copies of the revised blueprints... contain some small changes to the location of the windows and doors' (fax bản sao các bản thiết kế đã sửa... chứa một số thay đổi nhỏ). Mục đích là cung cấp thông tin về các thay đổi.",
    '176': "Chi tiết trong bài: Oscar viết 'Please check the modifications and let me know if they are all right' (Vui lòng kiểm tra các sửa đổi). Đồng nghĩa với Examine documents (Xem xét tài liệu).",
    '177': "Chi tiết trong bài: 'Preview for members only: Thursday, March 10' (Buổi xem trước dành riêng cho thành viên: Thứ Năm, 10/3).",
    '178': "Chi tiết trong bài: '2 free tickets to The Taming of the Shrew can be won in the membership lottery' (Bạn có thể trúng 2 vé xem kịch miễn phí trong đợt rút thăm trúng thưởng).",
    '179': "Chi tiết trong bài: Thiệp mời dự sự kiện 'An Opening Party at Mulligan\\'s' (Tiệc khai trương tại Mulligan\\'s) và 'Mulligan\\'s Bar'. Đây là khai trương một quán bar mới.",
    '180': "Chi tiết trong bài: Thiệp mời ghi rõ sự kiện diễn ra vào 'Saturday, November 15th' (Thứ Bảy, ngày 15 tháng 11).",
    '181': "Chi tiết trong bài: Lịch chiếu có 'Saturday... matinees' (chiều T7) và 'Saturday evenings' (tối T7). Do đó vào thứ Bảy có 2 suất diễn (Two).",
    '182': "Chi tiết trong bài: Ông Stein viết: 'I\\'d like to get tickets for our entire department to see Romeo and Juliet' (mua vé xem Romeo and Juliet). Romeo & Juliet là một vở kịch (A play).",
    '183': "Suy luận từ bài: Ông Stein tính rằng 'If everyone goes, there will be just enough people for a 10% discount'. Chính sách ưu đãi ghi 'Groups of 15 or more receive 10% off' (nhóm từ 15 người trở lên giảm 10%). 'Just enough' (vừa đủ) tức là bộ phận có đúng 15 người.",
    '184': "Chi tiết trong bài: 'see if you can get tickets for opening night' (đặt vé cho đêm khai mạc). Lịch chiếu từ 'March 12-29', nên đêm khai mạc là ngày 12/3 (March 12).",
    '185': "Chi tiết trong bài: 'We can all take the subway to the theater together' (Chúng ta có thể đi tàu điện ngầm cùng nhau).",
    '186': "Chi tiết trong bài: Email của Liz Lopez gửi vào 'Monday, Sept. 11' và thông báo sẽ đến muộn buổi họp diễn ra vào 'next Friday' (thứ Sáu tới). Thứ Sáu đó chính là ngày 15/9 (vì 11 là T2, 12 T3, 13 T4, 14 T5, 15 là T6). Cuộc họp diễn ra vào Thứ Sáu (Friday).",
    '187': "Chi tiết trong bài (Dựa vào bản gốc): Trong chương trình sự kiện, 'Market Report' sẽ do Liz Lopez thuyết trình.",
    '188': "Chi tiết trong bài: 'Mark plans to have Polly begin by 10:00'. Mặc dù OCR không lấy đủ tên, đối chiếu với các lựa chọn thì phần thuyết trình của Polly (Hiring Procedures) bắt đầu lúc 10h.",
    '189': "Chi tiết trong bài: 'lunch will be served from 12:00 - 1:15 in Conference Room A' (bữa trưa sẽ được phục vụ tại Phòng Hội nghị A).",
    '190': "Chi tiết trong bài: Lịch ghi: 'reconvene immediately following lunch... to hear Patty\\'s presentation' (họp lại ngay sau giờ ăn trưa để nghe Patty trình bày). Bữa trưa kết thúc lúc 1:15, nên phần này bắt đầu lúc 1:15. Bài của Patty là Product Development.",
    '191': "Chi tiết trong bài: Takubo gửi email giới thiệu một văn phòng (I have an office to show you...) và thảo luận về giá thuê (rent), cũng như liên hệ với chủ nhà (landlord). Anh ta là đại lý môi giới bất động sản (Real estate agent).",
    '192': "Chi tiết trong bài: Ms. Choi viết 'a convenient location is important' (một vị trí thuận tiện là điều quan trọng).",
    '193': "Phép tính từ bài: Ms. Choi nói ngân sách là $2,000. Takubo trả lời tiền thuê 'is $500 more than the price you mentioned' (cao hơn $500 so với mức giá bạn đề cập). Do đó giá thuê là $2000 + $500 = $2500.",
    '194': "Chi tiết trong bài: Ms. Choi cần văn phòng 'available by the end of the month' (có sẵn vào cuối tháng). Takubo đáp lại 'The office will be available by the time you need it' (Văn phòng sẽ có sẵn vào thời điểm bạn cần). Tức là vào cuối tháng (By the end of this month).",
    '195': "Chi tiết trong bài: Takubo hẹn giờ: 'I can meet you at the office at 11:00' (Tôi có thể gặp bạn lúc 11:00).",
    '196': "Chi tiết trong bài: Mona Aamons viết: 'I have filled in the form... and am sending it with this letter... I do not foresee any difficulties in issuing this card' (Tôi gửi form đăng ký...). Mục đích là xin cấp thẻ tín dụng (To apply for a credit card).",
    '197': "Chi tiết trong bài: 'believe that my credit rating is good' (tin rằng điểm tín dụng của tôi RẤT TỐT). Do đó cô ấy nghĩ nó tốt (It is good).",
    '198': "Chi tiết trong bài: Phía ngân hàng từ chối vì 'insufficient time in your current address and excessive debt-to-income ratio' (có quá nhiều khoản nợ so với thu nhập). Đồng nghĩa với Too many debts.",
    '199': "Chi tiết trong bài: 'You may receive a copy of this report free of charge, provided you request it in writing directly from the credit evaluation service' (yêu cầu trực tiếp từ công ty đánh giá tín dụng - Equity Evaluations).",
    '200': "Chi tiết trong bài: Ngân hàng thông báo 'You may receive a copy of this report free of charge... within six calendar months' (Bạn có quyền yêu cầu nhận một bản báo cáo tín dụng MIỄN PHÍ). Chọn D."
}

data['5']['explanations'].update(deep_exp)

with open('reading_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Updated reading explanations for Test 5 (151-200)')
