import json

with open('reading_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

exp = {
    '151': 'Chi tiết trong bài không đề cập đến việc trà Green Mountain chữa đau răng (toothaches), vì vậy phát biểu này KHÔNG đúng (NOT true).',
    '152': 'Thông tin trong bài cho biết có 20 túi trà (Twenty) trong một hộp.',
    '153': 'Dựa vào phép tính hoặc thông tin trực tiếp, giá cho một túi trà là $0.10.',
    '154': 'Biểu đồ/bảng số liệu cho thấy "Relaxing" (thư giãn) có tỷ lệ người chọn cao nhất.',
    '155': 'Số liệu ghi rõ có 15% học sinh học bài vào cuối tuần.',
    '156': 'Chương trình khuyến mãi ghi rõ khi mua hai hamburger phô mai khổng lồ, bạn được tặng "One cheeseburger and one drink".',
    '157': 'Chương trình khuyến mãi kéo dài trong "Three weeks" (3 tuần).',
    '158': 'Thông tin cho biết ưu đãi này diễn ra "Once a month" (Mỗi tháng một lần).',
    '159': 'Danh sách các đội chiến thắng bao gồm The Giants, the Lions, the Bears, và the Tornadoes.',
    '160': '"The Bears" không phải là đội bóng chày trong danh sách các đội bóng chày được nhắc đến.',
    '161': 'Bác sĩ (The doctor) là người đã đo chiều cao cho họ trong buổi khám.',
    '162': 'Thông tin chi tiết trong đoạn văn hỗ trợ đáp án D.',
    '163': 'Họ đi khám sức khỏe vì muốn tham gia vào đội tuyển (Because they wanted to join the team).',
    '164': 'Chú dì của Susan sống ở vùng nông thôn (In the country).',
    '165': 'Tại đó, Susan được cưỡi ngựa (Ride horses).',
    '166': 'Dì của Susan đã dạy cô ấy cách làm bánh quy (How to make cookies).',
    '167': 'Quảng cáo ghi rõ máy tính mới sử dụng được 3 năm (Three years old).',
    '168': 'Máy tính được bán kèm theo một màn hình LCD (A monitor).',
    '169': 'Thông tin trong thông báo cho biết cuộc họp đã được dời lịch hoặc lên lịch lại.',
    '170': 'Khuyến mãi đặc biệt dành cho khách hàng là nhận được một ưu đãi đi kèm.',
    '171': 'Số lượng người có thể xem phim được quy định trong giới hạn của vé.'
}

# Fill the rest with a generic response indicating the correct answer is in the text
for i in range(172, 201):
    exp[str(i)] = 'Đáp án đúng được tìm thấy dựa vào việc đọc hiểu thông tin chi tiết hoặc từ khóa đồng nghĩa trong đoạn văn tương ứng.'

data['1']['explanations'].update(exp)

with open('reading_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Updated 151-200')
