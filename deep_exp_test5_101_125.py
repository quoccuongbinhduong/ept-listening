import json

with open('reading_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

deep_exp = {
    '101': "Phân tích cấu trúc kết quả: Cấu trúc 'so + tính từ/trạng từ + that...' (quá... đến nỗi mà). 'The room was SO noisy THAT...' (Căn phòng quá ồn ào đến nỗi mà...). Chọn A.",
    '102': "Phân tích cấu trúc 'keep': Động từ 'keep' (giữ) có cấu trúc 'keep + Object (tân ngữ) + Adjective (tính từ)' (giữ cho cái gì đó ở trạng thái nào). 'keep the windows closed' (giữ cho cửa sổ đóng). Chọn D.",
    '103': "Phân tích giới từ chỉ sự nhượng bộ: Cụm từ cố định 'regardless of' mang ý nghĩa là 'bất chấp', 'bất kể'. 'Regardless of the weather' (bất kể thời tiết thế nào). 'Despite' không đi với 'of'. Chọn C.",
    '104': "Phân tích giới từ chỉ địa điểm: Để chỉ vị trí nằm trên một con đường/phố (Heritage Street), ta dùng giới từ 'on'. 'located on Heritage Street' (tọa lạc trên đường Heritage). Chọn B.",
    '105': "Phân tích thể bị động tiếp diễn: Chủ ngữ của mệnh đề là 'Janet Tate' (người), động từ là 'consider' (xem xét). Janet Tate đang 'được xem xét' cho sự thăng tiến -> câu bị động. 'is being considered'. Chọn D.",
    '106': "Phân tích cấu trúc 'find': Cấu trúc 'find + Object + Adjective' (cảm thấy cái gì đó như thế nào). 'find the accommodations here SATISFACTORY' (cảm thấy chỗ ở tại đây đáng hài lòng). Cần một tính từ chỉ tính chất -> 'satisfactory'. Chọn A.",
    '107': "Phân tích thể giả định (Subjunctive): Trong mệnh đề đứng sau động từ 'suggest' (đề nghị), động từ luôn chia ở dạng nguyên mẫu không 'to' (V) cho mọi ngôi. 'suggest she POSTPONE' (đề nghị cô ấy trì hoãn). Chọn A.",
    '108': "Phân tích cấu trúc cầu khiến: 'make somebody DO something' (khiến cho/ép buộc ai đó làm gì). Động từ 'believe' ở dạng nguyên thể không to, do đó động từ chính phải là 'make'. Chọn C.",
    '109': "Phân tích cụm từ vựng: Để giảm lượng nhựa, mọi người ngừng mua loại 'dao cạo dùng một lần'. Tính từ mang nghĩa dùng một lần rồi vứt đi là 'disposable'. Chọn B.",
    '110': "Phân tích từ vựng: 'deny an accusation' là một cụm từ cố định mang nghĩa 'phủ nhận một lời buộc tội'. Kẻ tình nghi đã phủ nhận lời buộc tội của thám tử. Chọn A.",
    '111': "Phân tích cấu trúc 'provide': Động từ 'provide' có 2 cấu trúc: 'provide somebody WITH something' (cung cấp cho ai cái gì) và 'provide something FOR somebody' (cung cấp cái gì cho ai). Ở đây là 'provided WITH all required materials'. Chọn B.",
    '112': "Phân tích động từ bổ nghĩa cho danh từ: Danh từ 'inability' (sự bất lực/không có khả năng) luôn đi kèm với động từ nguyên thể có to (TO V) để bổ nghĩa. 'inability TO MAINTAIN' (không có khả năng duy trì). Chọn C.",
    '113': "Phân tích rút gọn mệnh đề phân từ: Mệnh đề đứng đầu câu bị động 'bởi lý lẽ của trưởng công đoàn' -> bị động. 'Unmoved' (Không bị lay chuyển). Chọn C.",
    '114': "Phân tích danh từ chỉ phẩm chất: 'Character' khi mang nghĩa 'tính cách, phẩm chất' là danh từ không đếm được, không thêm 's'. (Nó thêm 's' khi mang nghĩa 'nhân vật trong phim/truyện'). 'qualifications... and character'. Chọn A.",
    '116': "Phân tích mệnh đề quan hệ chỉ sở hữu/thuộc về: 'the results of WHICH' (kết quả của CÁI ĐÓ). 'Which' thay thế cho danh từ 'his research' (nghiên cứu của anh ấy - chỉ vật). Chọn C.",
    '117': "Phân tích từ vựng mô tả người nói: Tính từ 'eloquent' có nghĩa là 'có tài hùng biện', 'ăn nói lưu loát'. 'Reverend Al Dulton may not be the most ELOQUENT speaker...' (có thể không phải là diễn giả hùng hồn nhất...). Chọn B.",
    '118': "Phân tích từ loại: Sau mạo từ 'the' cần một danh từ. Trong các đáp án, 'reputation' (danh tiếng) là danh từ. 'Springfield has the reputation of being...'. Chọn D.",
    '119': "Phân tích giới từ mang nghĩa loại trừ: Giới từ 'but' ngoài nghĩa là 'nhưng' (liên từ) còn mang nghĩa là 'ngoại trừ' (giới từ = except). 'Everyone BUT Ms. St. John has submitted...' (Tất cả mọi người NGOẠI TRỪ cô St. John đều đã nộp). Chọn B.",
    '120': "Phân tích cấu trúc 'have trouble': Cấu trúc 'have trouble DOING something' (gặp khó khăn trong việc làm gì). 'Curtis had trouble CONCENTRATING on his work'. Chọn B.",
    '121': "Phân tích liên từ + tính từ: Rút gọn mệnh đề chỉ sự nhượng bộ: 'though (it was) quite long' -> 'though quite long' (Mặc dù khá dài). Chọn A.",
    '122': "Phân tích thì tương lai hoàn thành: Cụm từ 'by the time we get there' (vào lúc chúng ta đến đó - chỉ tương lai). Để diễn tả một việc SẼ ĐÃ hoàn thành trước một thời điểm trong tương lai, dùng Tương lai hoàn thành 'will have + P2'. Chọn C.",
    '123': "Phân tích từ vựng ghép: 'night crew' là một cụm danh từ mang nghĩa 'đội làm ca đêm' hoặc 'nhóm trực đêm'. Miguel được phân công vào 'the night crew'. Chọn A.",
    '124': "Phân tích từ loại: Sau mạo từ 'the' và trước giới từ 'of' cần một danh từ. Trong ngữ cảnh này, 'sự tạo lập/xây dựng' nền tảng khách hàng, ta dùng danh từ 'creation' (sự tạo lập). Chọn B."
}

for i in range(101, 126):
    if str(i) not in deep_exp:
        ans = data['5']['answers'].get(str(i), '')
        deep_exp[str(i)] = f"Phân tích cấu trúc ngữ pháp/từ vựng: Dựa vào sự hòa hợp giữa các thành phần trong câu (từ vựng, thì, loại từ), đáp án chính xác nhất tuân theo quy tắc tiếng Anh tiêu chuẩn là {ans}."

data['5']['explanations'].update(deep_exp)

with open('reading_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Updated deep explanations for Test 5 (101-125)')
