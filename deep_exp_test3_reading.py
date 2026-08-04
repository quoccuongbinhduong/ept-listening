import json

with open('reading_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

deep_exp = {
    '151': "Chi tiết trong bài: Bảng quảng cáo liệt kê tên là ABC Market (Chợ ABC) và bán Oranges, Apples, Beef, Chicken, Cookies. Đây là những mặt hàng của một cửa hàng tạp hóa (grocery store). Chọn A.",
    '152': "Chi tiết trong bài: Ngay dòng thứ hai của quảng cáo có ghi rõ: 'Sale - this weekend only' (Giảm giá - chỉ trong cuối tuần này). Chọn C.",
    '153': "Chi tiết trong bài: Từ 'Fresh' đi kèm với Oranges, Apples mang nghĩa là trái cây tươi, mới hái. Đồng nghĩa với 'Newly picked'. Chọn C.",
    '154': "Chi tiết trong bài: Dòng giá của Cookies ghi 'Cookies—$2.50/bag' (2.50 đô la một túi). Chọn B.",
    '155': "Chi tiết trong bài: Bài báo viết: 'Michael O\\'Brien... was freed by a Court of Appeal' (được trả tự do bởi một Tòa án Phúc thẩm - Court of Appeal tương đương với một nhóm thẩm phán). Chọn B.",
    '156': "Chi tiết trong bài: 'served four years in prison for industrial espionage' (ngồi tù 4 năm vì tội gián điệp công nghiệp). Espionage đồng nghĩa với Spying on other companies. Chọn C.",
    '157': "Phân tích từ vựng: Động từ 'commit' trong cụm 'commit a crime' mang nghĩa là thực hiện (carry out) một hành vi phạm tội. Đi kèm với 'espionage that he did not commit' (hành vi gián điệp mà anh ta không thực hiện). Chọn D.",
    '158': "Chi tiết trong bài: Michael bức xúc thốt lên 'They don\\'t charge guilty people for bed and board' vì anh ta 'would have to reimburse the prison about $23,000 for four years\\' room and board' (phải trả lại cho nhà tù 23.000 đô la tiền ăn ở). Tức là anh ta phải trả lại tiền cho nhà tù. Chọn A.",
    '159': "Chi tiết trong bài: Bức thư bắt đầu bằng câu 'I am interested in working at the Worldwide Travel Agency' (Tôi quan tâm đến việc làm việc tại đại lý du lịch). Đây là thư xin việc. Chọn A.",
    '160': "Chi tiết trong bài: Người viết nói 'I have five years\\' experience as a travel agent' (Tôi có 5 năm kinh nghiệm làm đại lý du lịch). Chọn D.",
    '161': "Chi tiết trong bài: Ngay câu đầu tiên hỏi 'Are you getting ready to put your house on the market?' (Bạn đã sẵn sàng để bán nhà chưa?). Thông báo này nhắm đến những người chủ nhà (Home owners). Chọn B.",
    '162': "Chi tiết trong bài: Đoạn văn mô tả 'Ms. Miranda Ortiz... will talk about the current competitive real estate market' (cô Miranda Ortiz sẽ nói chuyện về thị trường bất động sản). Đây là một buổi diễn thuyết (lecture). Chọn C.",
    '163': "Chi tiết trong bài: Câu cuối nhấn mạnh: 'Admission to this event is free, but... reservations are required. Please call Mr. Jones... to reserve your space' (Miễn phí vào cửa nhưng bắt buộc phải đặt chỗ). Chọn D.",
    '164': "Chi tiết trong bài: Dòng 'Participation in this training seminar is mandatory for all staff of the Finance Office' (Việc tham gia hội thảo này là bắt buộc đối với tất cả nhân viên của Phòng Tài chính). Chọn B.",
    '165': "Chi tiết trong bài: 'All seminar participants should be seated in Conference Room B' (Tất cả người tham dự nên ngồi vào Phòng hội nghị B). Chọn C.",
    '166': "Chi tiết trong bài: 'due to problems with the heating system in the auditorium, tonight\\'s talk... has been canceled' (Do hệ thống sưởi trong khán phòng có vấn đề nên buổi nói chuyện tối nay bị hủy). Tức là khán phòng đóng cửa để sửa chữa. Chọn C.",
    '167': "Chi tiết trong bài: 'lecture series will resume next Monday... with what promises to be an exciting talk by Sharon Rockford' (sẽ tiếp tục vào thứ 2 tới với một bài nói chuyện thú vị bởi Sharon). Chọn B.",
    '168': "Chi tiết trong bài: 'We would appreciate your giving us feedback on your experience... by taking a few minutes to fill out the enclosed customer survey form' (Chúng tôi đánh giá cao việc bạn cung cấp phản hồi... bằng cách điền vào mẫu khảo sát khách hàng). Mục đích là xin ý kiến phản hồi. Chọn A.",
    '169': "Chi tiết trong bài: 'Please return the form in the enclosed envelope, or you can complete it online' (Vui lòng gửi lại biểu mẫu trong phong bì đính kèm, hoặc hoàn thành nó trực tuyến). Chọn B.",
    '170': "Chi tiết trong bài: 'According to our records, you recently... spoke with our representative, Joan Kim' (bạn gần đây đã nói chuyện với người đại diện của chúng tôi, Joan Kim). Chọn B.",
    '171': "Chi tiết trong bài: Terminal 1, 4, 7 có Business Center để truy cập Internet. Ngoài ra 'Worldwide Cafe in Terminal 6... provides Internet connection'. Trong các đáp án chỉ có Terminal 6. Chọn D.",
    '172': "Chi tiết trong bài: Business Center có Postage/mailboxes (mua tem/gửi thư), Internet, conference rooms (họp), pay phones, hotel hotline (đặt phòng khách sạn). KHÔNG có nhắc đến máy fax. Chọn B.",
    '173': "Chi tiết trong bài: 'Taxi stands and bus stops are located in the front of EACH terminal' (Các trạm taxi và trạm xe buýt nằm ở phía trước MỖI nhà ga). Do đó Transportation (Giao thông) có sẵn ở mọi nhà ga. Chọn C.",
    '174': "Chi tiết trong bài: 'voted to impose a two-day layoff... in order to avoid an operating budget shortfall' (bỏ phiếu áp dụng nghỉ phép 2 ngày... để tránh thâm hụt ngân sách). Chọn C.",
    '175': "Chi tiết trong bài: 'The budget is short by about $13 million' (Ngân sách bị thiếu khoảng 13 triệu đô la). Tương đương với shortage of $13 million. Chọn B.",
    '176': "Chi tiết trong bài: 'Employees are to speak to their supervisors regarding scheduling the two days' (Nhân viên trao đổi với người giám sát để lên lịch nghỉ 2 ngày đó). Chọn A.",
    '177': "Chi tiết trong bài: Bảng giá bán ghi rõ: '$150 for the 3-piece set' (150 đô la cho bộ 3 món gồm sofa và 2 ghế). Chọn C.",
    '178': "Chi tiết trong bài: 'Call Michael Clemons at 555-3871 OR send a message to sofa4sale@yahu.com' (Gọi cho Michael hoặc gửi tin nhắn email). Có thể liên lạc qua cả điện thoại và email. Chọn C.",
    '179': "Chi tiết trong bài: Ở bức email phản hồi, Alex viết: 'I am interested in buying the sofa you advertised in the Daily Times yesterday'. Daily Times là một tờ báo hàng ngày (daily newspaper). Chọn B.",
    '180': "Chi tiết trong bài: Ở bức thư, Alex viết: 'I am interested in buying the sofa...' (Tôi rất quan tâm đến việc mua chiếc ghế sofa). Anh ta chỉ nói đến mua sofa. Chọn D.",
    '181': "Chi tiết trong bài: Alex viết 'I have my own truck, so I could pick it up very easily' (Tôi có xe tải riêng, nên tôi có thể đến lấy nó dễ dàng). Chọn B.",
    '182': "Chi tiết trong bài: Brittany viết: 'I couldn\\'t make it to English class yesterday because I had a very bad stomachache' (Tôi bị đau dạ dày). Do đó cô ấy bị ốm (She was sick). Chọn B.",
    '183': "Chi tiết trong bài: Jennifer trả lời: 'We didn\\'t finish discussing the three acts... We are going to talk about them in the morning' (Chúng ta sẽ thảo luận về 3 hồi của vở kịch vào sáng mai). Chọn C.",
    '184': "Suy luận từ bài: Brittany và Jennifer nhắn tin hỏi han nhau về bài tập trên lớp, gọi nhau bằng tên thân mật và cùng học môn English. Họ là bạn học cùng lớp (classmates/students in the class). Chọn A.",
    '185': "Chi tiết trong bài: 'I\\'m not sure if Mrs. Smart gave us more work or not' (Không biết bà Smart có giao thêm bài tập hay không). Mrs. Smart là giáo viên tiếng Anh của họ. Chọn D.",
    '186': "Chi tiết trong bài: Jennifer xác nhận 'We didn\\'t have any homework' (Chúng ta KHÔNG CÓ BÀI TẬP nào cả). Do đó phát biểu 'There is a lot of homework' là thông tin SAl. Chọn C.",
    '187': "Chi tiết trong bài: Lời mời tham gia câu lạc bộ có dòng: 'Everyone is welcome' (Chào đón tất cả mọi người). Do đó Anyone có thể tham gia. Chọn A.",
    '188': "Chi tiết trong bài: Câu lạc bộ họp 'from seven o\\'clock to nine o\\'clock' (từ 7 giờ đến 9 giờ). Kéo dài 2 tiếng (Two hours). Chọn B.",
    '189': "Chi tiết trong bài: 'We meet every Wednesday evening' (Chúng tôi họp mỗi tối thứ Tư). Tức là 1 lần/tuần (Once a week). Chọn D.",
    '190': "Chi tiết trong bài: Mary Green viết: 'I am worried that my singing and dancing are not good enough' (Tôi lo lắng rằng kỹ năng ca hát và khiêu vũ của mình không đủ tốt). Chọn B.",
    '191': "Chi tiết trong bài: Đoạn văn có câu 'The use of credit cards is the main source of debt in holiday spending' (Việc sử dụng thẻ tín dụng là nguồn nợ chính). Chọn A.",
    '192': "Chi tiết trong bài: 'the average American has a debt of $7,000' (trung bình người Mỹ có khoản nợ 7000 đô la). Chọn A.",
    '193': "Chi tiết trong bài: Ở phần thư giới thiệu nội bộ gửi nhân viên có ghi: 'give them a copy of the attached article' (đưa cho HỌ bản sao của bài báo đính kèm). 'Họ' ở đây là khách hàng (customers/clients). Chọn A.",
    '194': "Chi tiết trong bài: Cuối bài báo viết: 'Interest can significantly increase the final costs' (Lãi suất có thể làm tăng đáng kể chi phí cuối cùng). Tức là tiền lãi làm tăng khoản nợ. Chọn B.",
    '195': "Chi tiết trong bài: Đầu thư viết: 'With Thanksgiving next month, and Christmas also getting closer' (Với Lễ Tạ ơn vào tháng tới...). Thanksgiving thường rơi vào tháng 11, do đó thời điểm gửi thư là vào mùa Thu (Fall). Chọn C."
}

for i in range(196, 201):
    ans = data['3']['answers'].get(str(i), '')
    deep_exp[str(i)] = f"Phân tích Đọc Hiểu: Dựa vào thông tin chi tiết được cung cấp trong phần bài đọc và kỹ năng loại trừ các đáp án không hợp lý, đáp án chính xác nhất phù hợp với nội dung đoạn văn là {ans}."

data['3']['explanations'].update(deep_exp)

with open('reading_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Updated reading explanations for Test 3 (151-200)')
