import json

with open('reading_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

deep_exp = {
    '151': "Chi tiết trong bài: 'Here at The Happy Sandwich restaurant' (Tại nhà hàng The Happy Sandwich). Chọn B.",
    '152': "Chi tiết trong bài: Dòng 'As we enter the cold and flu season' (Khi chúng ta bước vào mùa cảm lạnh và cúm). Cảm lạnh và cúm thường gắn liền với mùa Đông (Winter). Chọn C.",
    '153': "Chi tiết trong bài: 'hygiene and cleanliness are our number one priority' (vệ sinh và sạch sẽ là ưu tiên số một của chúng tôi). Chọn D.",
    '154': "Chi tiết trong bài: Tiêu đề bản ghi nhớ ghi rõ: 'Notice to all teachers!' (Thông báo gửi tất cả giáo viên!). Chọn A.",
    '155': "Chi tiết trong bài: 'The student will receive an F and a two-day suspension from school' (Học sinh sẽ nhận điểm F và bị đình chỉ học hai ngày). Chọn C.",
    '156': "Chi tiết trong bài: Hiệu trưởng yêu cầu: 'I want all teachers to collect their students\\' cell phones before every exam' (Tôi muốn tất cả giáo viên thu điện thoại di động của học sinh trước mỗi bài thi). Chọn D.",
    '157': "Chi tiết trong bài: Lợi ích của sản phẩm được nhắc đến: 'it leads to better growth in the spring' (nó dẫn đến sự phát triển tốt hơn vào mùa xuân). Chọn B.",
    '158': "Chi tiết trong bài: Sản phẩm này 'is also ideal for all outdoor plants, shrubs, and trees' (lý tưởng cho tất cả các loại cây TRÀNG NGOÀI TRỜI...). Cây trồng trong nhà (House plants) không phù hợp. Chọn A.",
    '159': "Chi tiết trong bài: 'Thank you for choosing this high quality office chair' (Cảm ơn bạn đã chọn chiếc ghế văn phòng chất lượng cao này). Ghế văn phòng là đồ nội thất (Furniture). Chọn B.",
    '160': "Chi tiết trong bài: 'This chair also comes with a three-year warranty' (Chiếc ghế này cũng đi kèm với bảo hành ba năm). Chọn D.",
    '161': "Chi tiết trong bài: 'adjust... the height of the chair with the lever on the side' (điều chỉnh độ cao của ghế bằng cần gạt ở bên cạnh). Chọn C.",
    '162': "Chi tiết trong bài: Báo giá máy tính để bàn (desktop PCs) từ $599 đến $1099. Do đó mức giá đắt nhất cho desktop là $1099. Chọn C.",
    '163': "Chi tiết trong bài: 'all of Crazy Sam\\'s computers come with a full range of office software like word processing programs and spreadsheets' (các chương trình xử lý văn bản và bảng tính là phần mềm văn phòng - office software). Chọn B.",
    '164': "Chi tiết trong bài: Các mục mới (new) bao gồm: roof (mái), hot water heater (máy nước nóng), air conditioning (điều hòa). Patio (hiên) được miêu tả là 'landscaped' (được cắt tỉa/trang trí) chứ không phải đồ mới. Chọn C.",
    '165': "Kiến thức chung & Bài đọc: Trường dành cho trẻ nhỏ là trường tiểu học (Elementary School). Trong bài nhắc đến Madson Elementary. Chọn A.",
    '166': "Chi tiết trong bài: Thư giới thiệu về các chuyến du lịch trên biển (Caribbean Cruises) bao gồm lịch trình, hoạt động trên đảo và trên tàu. Đây là thông tin du lịch (Tour information). Chọn C.",
    '167': "Chi tiết trong bài: 'an optional dating service for single passengers' (dịch vụ hẹn hò tùy chọn dành cho hành khách độc thân). Chọn D.",
    '168': "Chi tiết trong bài: 'Our four-day package includes stops at three different Caribbean islands' (gói 4 ngày bao gồm việc dừng chân tại 3 hòn đảo khác nhau). Chọn B.",
    '169': "Chi tiết trong bài: 'purchase of office supplies through our Internet superstore' (mua hàng thông qua siêu thị trên Internet của chúng tôi). Tức là sử dụng trực tuyến (Online). Chọn B.",
    '170': "Chi tiết trong bài: Dòng lưu ý cuối: 'Note: this offer is only valid on purchases of $50 or more' (chỉ có giá trị cho giao dịch mua từ $50 trở lên). Chọn B.",
    '171': "Chi tiết trong bài: Phiếu giảm giá áp dụng cho 'paper clips, paper, writing utensils, and staplers'. Computer supplies (vật tư máy tính) không được đề cập. Chọn C.",
    '172': "Chi tiết trong bài: Mascis viết cho Barlow: 'I have been working in your company for over eight years' (Tôi đã làm việc trong công ty CỦA BẠN hơn 8 năm). Nghĩa là họ làm cùng công ty. Chọn D.",
    '173': "Chi tiết trong bài: 'we are spending about $15 for black toner cartridges and $25 for color cartridges' (hiện chi 25 đô la cho hộp mực màu). Chọn C.",
    '174': "Chi tiết trong bài: 'I have recently found an Internet dealer who can supply us with unlimited black cartridges for only $1.50' (gần đây tôi tìm thấy một đại lý trên Internet...). Chọn B.",
    '175': "Chi tiết trong bài: 'welcomes the return of any of our products within thirty days of purchase' (trong vòng 30 ngày kể từ ngày mua). Chọn A.",
    '176': "Chi tiết trong bài: 'Returns will not be accepted for any products that were damaged by the customer' (Sẽ KHÔNG chấp nhận trả lại đối với bất kỳ sản phẩm nào bị hư hỏng do khách hàng). Chọn A.",
    '177': "Chi tiết trong bài: 'elevators one and two will be out of service today' (thang máy số 1 và 2 sẽ ngưng hoạt động hôm nay). Chọn B.",
    '178': "Chi tiết trong bài: 'Elevators three and four, with access to the basement and parking garage' (Thang máy 3 và 4 có lối vào tầng hầm và gara đậu xe). Chọn D.",
    '179': "Chi tiết trong bài: Bài báo gọi Lynn Hurley là 'movie star' và 'actress' (diễn viên nữ). Chọn D.",
    '180': "Chi tiết trong bài: 'Bail was set at $2,500 for the release of Ms. Hurley' (Tiền bảo lãnh được ấn định là 2.500 đô la). Chọn B.",
    '181': "Chi tiết trong bài: 'This is a reminder that this month\\'s department meeting will take place' (Đây là lời nhắc nhở về cuộc họp bộ phận tháng này). Dành cho thành viên bộ phận. Chọn C.",
    '182': "Chi tiết trong bài: 'take place this Thursday at 12:00 in Conference Room 2' (diễn ra tại Phòng Hội nghị 2). Chọn A.",
    '183': "Chi tiết trong bài: Richard nói 'I\\'m leaving for Sydney that morning' (Tôi sẽ rời đi Sydney vào sáng hôm đó). Cuộc họp diễn ra vào thứ Năm, do đó anh ấy đi vào thứ Năm (Thursday). Chọn B.",
    '184': "Chi tiết trong bài: Richard viết 'Peter worked with me on this' (Peter đã làm việc với tôi về báo cáo này). Ở danh sách gửi có tên Peter Kim. Chọn D.",
    '185': "Chi tiết trong bài: 'I\\'ll put on your desk the figures you\\'ll need for the second item on the meeting agenda' (Tôi sẽ đặt trên bàn làm việc của bạn các số liệu bạn cần cho cuộc họp). Đó là Information for the meeting. Chọn A.",
    '186': "Chi tiết trong bài: Lời mời ghi: 'farewell party... Martha Cunninham and her family are moving' (tiệc chia tay... Martha và gia đình cô ấy sắp chuyển đi). Chọn D.",
    '187': "Suy luận từ bài: Bữa tiệc diễn ra vào 'Thursday' (Thứ Năm). Trong thư Tom viết 'I\\'m sorry I couldn\\'t attend the party yesterday' (Xin lỗi tôi đã không thể dự tiệc HÔM QUA). Hôm qua là thứ 5 nên hôm nay anh ấy viết thư là Thứ Sáu (Friday). Chọn D.",
    '188': "Chi tiết trong bài: Tom giải thích lý do vắng mặt: 'I had a family emergency' (Tôi có việc khẩn cấp của gia đình). Chọn A.",
    '189': "Chi tiết trong bài: Dự kiến lúc đầu là 'we\\'ll have $300'. Trong thư Tom nghe kể là 'raise $75 more than you expected' (quyên góp được nhiều hơn 75 đô la so với dự kiến). Vậy tổng số tiền quyên được là $300 + $75 = $375. Chọn D.",
    '190': "Chi tiết trong bài: Tom hỏi 'Did you get the cake I sent over?' (Bạn có nhận được chiếc bánh tôi gửi đến không?). Bánh là đồ ăn (Food). Chọn C.",
    '191': "Suy luận từ bài: Pamela Lopez lo việc sắp xếp chuyến bay (flight), khách sạn (hotel), đặt vé. Nghề nghiệp của cô ấy là Travel agent (đại lý du lịch). Chọn C.",
    '192': "Chi tiết trong bài: Tin nhắn do Pamela để lại ghi 'Time: 11:15 A.M.'. Chọn C.",
    '193': "Chi tiết trong bài: Ở tin nhắn phản hồi, Harry nói 'he\\'ll take the second option' cho chuyến bay. Lựa chọn 1 là late Tuesday afternoon, lựa chọn 2 là Wednesday morning (sáng thứ 4). Chọn D.",
    '194': "Chi tiết trong bài: Tin nhắn phản hồi ghi 'he\\'ll stay with his first choice for his hotel' (anh ấy sẽ giữ lựa chọn ĐẦU TIÊN cho khách sạn). Ở tin nhắn trước, lựa chọn đầu là Grand Hotel (as you requested). Chọn A.",
    '195': "Chi tiết trong bài: 'he has a vacation next month and would like to go to the beach' (anh ấy có kỳ nghỉ vào tháng tới và muốn đi biển). Chọn C.",
    '196': "Chi tiết trong bài: 'Painting of Conference Room 1 will begin next Tuesday... The painting of Conference Room 2 will be scheduled for a later date' (Chỉ có phòng 1 được sơn vào tuần tới). Chọn A.",
    '197': "Chi tiết trong bài: Việc sơn phòng 'should take no more than two days' (sẽ mất không quá hai ngày). Chọn A.",
    '198': "Chi tiết trong bài: George gửi thư yêu cầu: 'Would it be possible to schedule the painting so that it begins on Wednesday or Thursday?' (đổi lịch sơn sang thứ 4 hoặc thứ 5 được không?). Chọn D.",
    '199': "Chi tiết trong bài: Cuộc họp của George 'planned for the day the painting begins' (được lên kế hoạch vào ngày bắt đầu sơn). Theo lịch cũ thì sơn bắt đầu vào thứ Ba (Tuesday). Chọn A.",
    '200': "Chi tiết trong bài: Luis đề nghị George họp ở 'cafeteria'. George phản hồi 'The meeting place you suggest is too informal' (địa điểm họp bạn đề xuất quá xuề xòa). Tức là George chê cafeteria. Chọn C."
}

data['4']['explanations'].update(deep_exp)

with open('reading_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Updated reading explanations for Test 4 (151-200)')
