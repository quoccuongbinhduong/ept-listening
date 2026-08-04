import json

with open('reading_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

deep_exp = {
    '151': "Chi tiết trong bài: Bảng thống kê môn học yêu thích nhất (favorite class) cho thấy English có số lượng học sinh chọn cao nhất (35). Do đó English là môn học phổ biến nhất.",
    '152': "Chi tiết trong bài: Lý do phổ biến nhất số 1 là 'They liked the teacher' (Họ thích giáo viên). Chọn đáp án có ý nghĩa tương đương.",
    '153': "Chi tiết trong bài: Bảng thống kê môn học ít được yêu thích nhất (least favorite class) cho thấy History có số lượng học sinh chọn cao nhất (45).",
    '154': "Chi tiết trong bài: Đoạn miêu tả ngoại hình chú chó con: 'She is small and yellow with black spots' (Nó nhỏ, màu vàng và có đốm đen).",
    '155': "Chi tiết trong bài: Câu 'If you find her, please call us at 555-9837' (Nếu bạn tìm thấy nó, vui lòng gọi cho chúng tôi). Nghĩa là bạn chỉ gọi khi tìm thấy chú chó.",
    '156': "Chi tiết trong bài: Ngay đầu bức thư Jessica viết: 'I\\'m doing fine here at summer camp' (Mình vẫn khỏe khi ở trại hè).",
    '157': "Chi tiết trong bài: Lời chào cuối thư Jessica viết: 'See you next week!' (Hẹn gặp bạn vào tuần tới).",
    '158': "Chi tiết trong bài: Jessica miêu tả cảm giác lúc đầu: 'At first, I was scared of the water' (Lúc đầu, tôi rất sợ nước).",
    '159': "Chi tiết trong thực đơn: Tính tổng giá trị các món: A large cola ($1.50) + a hotdog ($2.00) = $3.50. Đây là mức giá cao nhất so với các lựa chọn còn lại trong đáp án.",
    '160': "Chi tiết trong thực đơn: Phần nước uống liệt kê: Soft Drinks (Cola, Lemon-Lime, Orange), Fresh Orange Juice, Lemon Iced Tea. Tổng cộng có 5 loại thức uống (3 loại nước ngọt + nước cam + trà chanh).",
    '161': "Chi tiết trong thực đơn: Một hamburger có giá $3.00, một ly Lemon Iced Tea nhỏ có giá $2.00. Tổng số tiền là $5.00.",
    '162': "Chi tiết trong thực đơn: Grape juice (nước ép nho) nằm trong mục Fresh Juice có giá $1.00. Đây là mức giá rẻ nhất trong các đáp án.",
    '163': "Chi tiết trong thực đơn: Coffee có giá $1.50, Iced Tea có giá $1.50. Tổng số tiền cho 2 món này là $3.00.",
    '164': "Chi tiết trong bài: Dòng thứ 2 ghi rõ: 'Our new address, starting April 1st, is...' (Địa chỉ mới của chúng tôi, bắt đầu từ ngày 1 tháng 4, là...).",
    '165': "Chi tiết trong bài: Địa chỉ mới được ghi là '45 Oakland Avenue Suite 10'. Do đó văn phòng mới nằm trên đường Oakland Avenue.",
    '166': "Chi tiết trong bài: Dòng cuối cùng khẳng định: 'Our phone number will stay the same' (Số điện thoại của chúng tôi sẽ không thay đổi).",
    '167': "Chi tiết trong bài: Câu 'On the express train it will take only three hours' (Trên chuyến tàu tốc hành, nó sẽ chỉ mất ba giờ).",
    '168': "Chi tiết trong bài: Bài đọc có câu: 'There will also be three regular trains' (Cũng sẽ có 3 chuyến tàu thường).",
    '169': "Chi tiết trong bài: Câu cuối đoạn văn nêu rõ lý do: 'Many people will prefer the regular trains because the tickets are cheaper' (Nhiều người sẽ thích tàu thường hơn vì vé rẻ hơn).",
    '170': "Phân tích từ vựng: Từ 'service' trong ngữ cảnh vận tải (begin service) đồng nghĩa với 'operation' (sự hoạt động/khai thác tuyến đường).",
    '171': "Chi tiết trong bài: 'Business Times' có tùy chọn đăng ký (subscribe) theo tháng/năm, và được gửi về nhà mỗi tháng. Đây là đặc điểm của một tờ tạp chí (magazine).",
    '172': "Chi tiết trong bài: Trong phần điền thông tin, mục Check one (chọn thời hạn) có đánh dấu vào 'one year'. Mức giá tương ứng cho một năm là $45.",
    '173': "Chi tiết trong bài: Tại mục Payment method (Phương thức thanh toán), có một dấu đánh vào ô 'money order'.",
    '174': "Chi tiết trong bài: Đoạn 2 ghi rõ: 'We have reserved a party room at O\\'Byrne\\'s Pub... for the reception' (Chúng tôi đã đặt trước một phòng tiệc tại O\\'Byrne\\'s Pub cho tiệc chiêu đãi).",
    '175': "Chi tiết trong bài: Đám cưới là của Jennifer và Michael, chứ không phải của bố mẹ họ (Their parents are getting married là thông tin SAl).",
    '176': "Dựa vào biểu đồ cân nặng (chart) trong bài thi, trọng lượng của Peter vào tháng 6 (Jun) giảm xuống mức 85kg trước khi tăng lại. Đáp án được xác định từ cột tương ứng của tháng 6.",
    '177': "Dựa vào biểu đồ cân nặng (chart) trong bài thi, điểm xuất phát ở đầu năm (Jan) của Peter nằm ở vạch 100kg.",
    '178': "Chi tiết trong bài: Peter kể lại 'In January and February, I began swimming twice a week' (Vào tháng 1 và tháng 2, tôi bắt đầu đi bơi hai lần một tuần).",
    '179': "Chi tiết trong bài: Peter kể 'In May, I spent a week at the gym and gained back some of this lost weight' (Vào tháng 5, tôi dành 1 tuần ở phòng tập và bị tăng cân lại...). Mặc dù ở phòng tập nhưng lại là nơi anh ấy tăng cân.",
    '180': "Chi tiết trong bài: Người viết nói 'My husband, two children, and I' (Chồng tôi, hai con và tôi). Do đó người viết mẫu quảng cáo này là người vợ (The wife).",
    '181': "Chi tiết trong bài: Lý do được nêu rõ ở câu đầu tiên: 'because we are moving to Hong Kong next summer' (bởi vì chúng tôi sẽ chuyển đến Hồng Kông vào mùa hè tới).",
    '182': "Chi tiết trong bài: Họ cần gia sư 3 buổi 1 tuần (Thứ 2, 4, 5), mỗi buổi 1 tiếng. Trả $10/giờ -> Tổng cộng 1 tuần là $30.",
    '183': "Chi tiết trong bài bức thư của Lily: 'I taught Chinese in my home country' (Tôi đã dạy tiếng Trung ở quê nhà của tôi). Quê nhà cô ấy là Hồng Kông. Do đó cô ấy từng là giáo viên.",
    '184': "Chi tiết trong bài: Dưới mục Men\\'s T-shirt (Áo thun nam), phần Colors liệt kê: 'white, green, blue'.",
    '185': "Chi tiết trong bài: Áo nam giá $9.95. Với $20 bạn có thể mua 2 cái. Khuyến mãi 'Buy 2, get one free' (Mua 2 tặng 1). Vậy với $20 bạn nhận được tổng cộng 3 áo nam.",
    '186': "Chi tiết trong bài: Áo nam có trắng, xanh lá, xanh dương. Áo nữ có trắng, đỏ, vàng, xanh dương. Áo trẻ em có đỏ, vàng, trắng. Màu duy nhất cả 3 loại áo đều có là 'White' (Trắng).",
    '187': "Chi tiết trong bài: Lời cảm ơn mở đầu thư: 'To thank you for being one of our regular customers...' (Để cảm ơn vì bạn là một trong những khách hàng thường xuyên của chúng tôi...).",
    '188': "Chi tiết trong bài quảng cáo: Nhìn vào bảng giá, vé đi Seoul có giá cao nhất ($699) so với các địa điểm khác.",
    '189': "Chi tiết trong bài: George chỉ có $300, vậy anh ấy chỉ có thể chọn địa điểm có giá thấp hơn $300. Nhìn vào bảng giá, chỉ có Paris ($299) là phù hợp.",
    '190': "Chi tiết trong bài: Thời gian áp dụng giá đặc biệt là 'From May 15th - June 30th only'. Do đó, ngày 1 tháng 7 (July 1st) hoặc các ngày trong tháng 7 (như July 30th) sẽ không được áp dụng.",
    '191': "Chi tiết trong bài: Cuối thông báo có ghi: 'We will pay $10 commission for every customer...' (Chúng tôi sẽ trả 10 đô la hoa hồng cho mỗi khách hàng...). Nếu bán được cho 20 khách hàng thì đại lý nhận được 20 * $10 = $200.",
    '192': "Chi tiết trong bài: Thư của Sue gửi ngày 23/6. Sue viết 'She was born last month' (Cô bé được sinh ra vào tháng trước). Tháng trước của tháng 6 là tháng 5 (May).",
    '193': "Chi tiết trong bài: Trong thư có nhắc đến con gái mới sinh ('new daughter') và anh trai của cô bé ('her older brother'). Vậy George có 2 người con.",
    '194': "Chi tiết trong bài: Ở bức thư đầu tiên, Sue nói 'Thanks for sending those pictures' (Cảm ơn vì đã gửi những bức ảnh đó).",
    '195': "Chi tiết trong bài: Trong bức thư phản hồi, George nói 'This office is so busy today' (Văn phòng hôm nay rất bận rộn). Điều này chứng tỏ anh ấy đang viết thư tại văn phòng.",
    '196': "Chi tiết trong bài: Quảng cáo tìm người cho các vị trí Cook, Waiter có yêu cầu 'experience required' (yêu cầu kinh nghiệm) hoặc 'experience preferred' (ưu tiên có kinh nghiệm). Tức là tuyển những người đã từng làm việc trong nhà hàng.",
    '197': "Chi tiết trong bài: Tổng số lượng tuyển: Cook (2) + Waiter (2) + Cashier (1) + Dishwasher (1) = 6 người (Six).",
    '198': "Chi tiết trong bài: Quảng cáo tuyển dụng liệt kê các vị trí: Cook, Waiter, Cashier, Dishwasher. Không có vị trí Quản lý (Manager).",
    '199': "Chi tiết trong bài: Ứng viên Mike viết 'I am a cook with over seven years\\' experience' (Tôi là một đầu bếp với hơn 7 năm kinh nghiệm).",
    '200': "Chi tiết trong bài: Mike ứng tuyển vị trí Đầu bếp (Cook), không phải Quản lý (Manager). Do đó phát biểu 'Mike wants to be manager' là SAl."
}

data['2']['explanations'].update(deep_exp)

with open('reading_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Updated reading explanations for Test 2 (151-200)')
