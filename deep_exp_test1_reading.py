import json

with open('reading_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

deep_exp = {
    '151': "Chi tiết trong bài: Trà Green Mountain 'Good for colds, headaches, and even stomachaches!' (Tốt cho cảm lạnh, đau đầu và thậm chí đau dạ dày). Không hề nhắc đến đau răng (toothaches), do đó B là SAI (NOT true). Chọn B.",
    '152': "Chi tiết trong bài: 'One box of fifty tea bags is only $5.00' (Một hộp gồm năm mươi túi trà). 'Fifty' là 50. Chọn D.",
    '153': "Phép tính từ bài: Một hộp 50 túi trà giá 5 đô la ($5.00). Vậy mỗi túi trà giá: 5 / 50 = $0.10. Chọn B.",
    '154': "Chi tiết trong bài: 'The most popular response was watching movies, with 35 percent' (Câu trả lời phổ biến nhất là xem phim, với 35 phần trăm). Chọn A.",
    '155': "Chi tiết trong bài: 'Study: 10%' (Học bài: 10%). Chọn D.",
    '156': "Chi tiết trong bài: 'Buy two giant cheeseburgers to get one cheeseburger and one drink free!' (Mua hai bánh cheeseburger khổng lồ sẽ được tặng một cheeseburger và một đồ uống miễn phí). Chọn B.",
    '157': "Chi tiết trong bài: 'The Summer Special Offer will last all summer, from June 1st to August 31st' (từ 1/6 đến 31/8, tức là 3 tháng). Chọn C.",
    '158': "Chi tiết trong bài: Chương trình được gọi là 'annual Summer Special Offer' (Khuyến mãi đặc biệt Mùa hè HÀNG NĂM). Tức là diễn ra mỗi năm một lần (Every year). Chọn A.",
    '159': "Chi tiết trong bài: 'The Giants crushed the Bluebirds... Yellow Socks beat the Lions... Tiger fans... happy with their team\\'s victory... the Superstars won again'. Các đội thắng là Giants, Yellow Socks, Tigers, và Superstars. Chọn C.",
    '160': "Chi tiết trong bài: Mục 'Soccer' (bóng đá) ghi 'Tornadoes 0-2 Superstars'. Do đó Superstars là đội bóng đá chứ không phải bóng chày (baseball). Chọn A.",
    '161': "Chi tiết trong bài: 'the army doctor began checking their height and weight' (bác sĩ quân y bắt đầu kiểm tra chiều cao và cân nặng của họ). Chọn B.",
    '162': "Chi tiết trong bài: 'John was a bit embarrassed... Andy was also embarrassed' (John hơi xấu hổ... Andy cũng xấu hổ). Chọn D.",
    '163': "Chi tiết trong bài: 'John and his three friends decided to join the army' (John và ba người bạn quyết định gia nhập quân đội). Chọn C.",
    '164': "Chi tiết trong bài: 'I\\'m at my aunt and uncle\\'s house in the country' (Tôi đang ở nhà chú dì ở nông thôn). Chọn A.",
    '165': "Chi tiết trong bài: Susan viết 'I ride horses every day with my uncle' (Tôi cưỡi ngựa mỗi ngày cùng chú). Chọn D.",
    '166': "Chi tiết trong bài: Susan viết 'She taught me how to make chocolate chip cookies' (Dì đã dạy tôi cách làm bánh quy sô-cô-la chip). Chọn A.",
    '167': "Chi tiết trong bài: Mẩu quảng cáo ghi 'Pentium 4 — only 3 years old' (chỉ mới 3 năm tuổi). Chọn B.",
    '168': "Chi tiết trong bài: Quảng cáo ghi 'Include 19-inch LCD monitor' (Bao gồm màn hình LCD 19-inch). Chọn A.",
    '169': "Chi tiết trong bài: 'Tuesday\\'s Movie Club meeting... will be moved to Friday at 3:00 p.m.' (buổi họp thứ Ba sẽ được chuyển sang thứ Sáu). Chọn C.",
    '170': "Chi tiết trong bài: 'as part of our special offer, this week you can bring one friend for free' (ưu đãi đặc biệt tuần này bạn có thể dẫn theo một người bạn miễn phí). Chọn D.",
    '171': "Chi tiết trong bài: 'We have seating for only 300 people' (Chúng tôi chỉ có chỗ ngồi cho 300 người). Chọn B.",
    '172': "Chi tiết trong bài: John viết 'Thank you for the new bike that you gave me' (Cảm ơn bà vì chiếc xe đạp mới bà tặng cháu). Bike = bicycle. Chọn D.",
    '173': "Chi tiết trong bài: Câu cuối thư 'I promise that I will take good care of it' (Cháu hứa sẽ chăm sóc nó cẩn thận). Chọn B.",
    '174': "Chi tiết bảng: Có 125 nữ (girls) từ Châu Á, và 25 nam (boys) từ Úc. Rõ ràng 125 > 25 (Nhiều nữ từ Châu Á hơn nam từ Úc). Chọn B.",
    '175': "Chi tiết bảng: Châu Á (Asia) có 100 nam + 125 nữ = 225 học sinh, đông nhất trong tất cả các khu vực. Chọn A.",
    '176': "Suy luận từ bảng: Hoa Kỳ và Canada thuộc Bắc Mỹ (N. America). Số lượng học sinh là 45 + 50 = 95. Chọn C.",
    '177': "Chi tiết trong bài: 'He went missing on Tuesday, two days ago' (Chú chó đi lạc vào thứ Ba, cách đây HAI NGÀY). Nếu thứ Ba là 2 ngày trước, thì hôm nay là thứ Năm (Thursday). Chọn B.",
    '178': "Chi tiết trong bài: 'He is wearing a blue-and-red collar' (Nó đang đeo một chiếc vòng cổ màu xanh-và-đỏ). Chọn C.",
    '179': "Chi tiết trong bài: 'We have had him for six years' (Chúng tôi đã nuôi nó được 6 năm). Chọn C.",
    '180': "Chi tiết trong bài: Sarah viết 'I got a new job working at a toy company' (Tôi vừa nhận một công việc mới tại một công ty đồ chơi). Chọn B.",
    '181': "Chi tiết trong bài: Sarah viết 'I have a vacation next month' (Tôi có kỳ nghỉ vào tháng tới). Chọn C.",
    '182': "Chi tiết trong bài: Sarah bảo Jenny 'you should come visit me soon' và 'Call me soon!' (hãy gọi cho tôi sớm). Chọn A.",
    '183': "Chi tiết trong bài: Jenny đáp lại lời mời thăm vào tháng tới (next month) rằng 'I have to find a part-time job, so I won\\'t have much free time' (tôi phải tìm việc nên không có thời gian). Cô ấy hẹn 'Maybe... during the summer vacation to visit you'. Vậy A (Jenny sẽ tới thăm vào tháng sau) là KHÔNG đúng. Chọn A.",
    '184': "Chi tiết trong bảng: Nhiệt độ cao nhất trong các thành phố được liệt kê là Singapore (27°C). Chọn C.",
    '185': "Chi tiết trong bảng: Nhiệt độ thấp nhất là Bắc Kinh / Beijing (-4°C). Chọn A.",
    '186': "Chi tiết trong bảng: Jakarta được dự báo 'heavy rain' (mưa lớn), trong khi Singapore chỉ 'rainy' (có mưa). Do đó Jakarta có lượng mưa nhiều nhất. Chọn C.",
    '187': "Chi tiết trong bài: Thư của Marilyn James ghi 'Your trip starts in Beijing' (Chuyến đi của bạn bắt đầu ở Bắc Kinh). Suy ra cô ấy xem thời tiết để đi du lịch (taking a trip). Chọn B.",
    '188': "Chi tiết trong bài: Biển báo ghi 'Open: May 31st — August 31st' (Mở cửa từ 31/5 đến 31/8). Do đó ngày 5/4 (April 5th) biển KHÔNG mở cửa. Chọn B.",
    '189': "Chi tiết trong bài: Luật ghi rõ 'Children under eight years must be with an adult' (Trẻ em dưới tám tuổi phải đi cùng người lớn). Tức là không được đi một mình. Chọn D.",
    '190': "Chi tiết trong bài: Luật thi đấu ghi 'entrants must be over sixteen' (trên 16 tuổi) và 'one male and one female' (một nam, một nữ). Lựa chọn C (A man and a woman) thỏa mãn. Chọn C.",
    '191': "Chi tiết trong bài: Bản ghi nhớ dặn nhân viên cứu hộ 'Please do not watch the competition' (Vui lòng KHÔNG xem cuộc thi). Do đó phương án A (Lifeguards should watch...) là SAI. Chọn A.",
    '192': "Suy luận từ bảng hướng dẫn: Tầng 5 (5th Floor) bán 'Antique and Modern Furniture' (Đồ nội thất). Bàn (table) là đồ nội thất. Chọn D.",
    '193': "Suy luận từ bảng hướng dẫn: Tầng 1 (1st Floor) bán 'Computers and Home Electronics' (Máy tính và Đồ điện tử gia dụng). Đầu DVD (DVD player) là đồ điện tử gia dụng. Chọn C.",
    '194': "Chi tiết trong bài: '40% off all his-and-hers cardigans (10:30-11:30)' (giảm 40% cho áo khoác len từ 10:30 đến 11:30 sáng). Cardigan là một loại áo len (sweater). Chọn A.",
    '195': "Chi tiết trong bài: Quản lý viết 'We have made a lot of changes and we would like to invite you to take a closer look' (Chúng tôi đã thực hiện rất nhiều thay đổi...). Chọn A.",
    '196': "Chi tiết bảng điểm: Môn Music (Âm nhạc) đạt điểm A+ (cao nhất). Chọn D.",
    '197': "Chi tiết bảng điểm: Môn Science (Khoa học) đạt điểm C (thấp nhất). Chọn C.",
    '198': "Chi tiết bảng điểm: Môn English được B, môn Art được B. Do đó hai môn này cùng điểm. Chọn D.",
    '199': "Chi tiết trong bài: Phụ huynh viết 'We are very happy to see Mary received an A for Math... Last time, she received a C' (Rất vui vì Toán được A... Lần trước con bé bị C). Điểm đã tốt hơn rất nhiều. Chọn C.",
    '200': "Chi tiết trong bài: Phụ huynh lo lắng 'We are worried that she won\\'t get into a good university' (Chúng tôi lo rằng con bé sẽ không đậu vào một trường đại học tốt). Chọn A."
}

data['1']['explanations'].update(deep_exp)

with open('reading_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Updated reading explanations for Test 1 (151-200)')
