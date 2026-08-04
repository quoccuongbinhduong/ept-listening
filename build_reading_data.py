import json

with open('reading_answers.json', 'r', encoding='utf-8') as f:
    answers = json.load(f)

# PDF Pages mapping (1-indexed for the URL hash, but let's just supply the page number for each test)
# Looking at the PDF:
# Test 1 starts at page 15.
# Test 2 starts at page 28.
# Test 3 starts at page 42.
# Test 4 starts at page 57.
# Test 5 starts at page 71.

test_data = {
    "1": {
        "title": "Practice Test 1",
        "file": "reading_test_1.pdf",
        "answers": answers.get("1", {}),
        "explanations": {
            "101": "Động từ 'belong' (thuộc về) là động từ trạng thái (stative verb), không dùng ở thì tiếp diễn. Chủ ngữ 'The car' số ít nên chia là 'belongs'.",
            "102": "Trạng từ chỉ tần suất 'sometimes' (thỉnh thoảng) được dùng để diễn tả thói quen ở hiện tại đơn.",
            "103": "Động từ 'like' (thích) là động từ trạng thái, ít khi dùng ở thì tiếp diễn. Chủ ngữ 'I' đi với 'like' ở hiện tại đơn.",
            "104": "Thì hiện tại tiếp diễn 'are arriving' có thể diễn tả một lịch trình, dự định chắc chắn sẽ xảy ra trong tương lai (at two o'clock tomorrow).",
            "105": "Một hành động đang xảy ra trong quá khứ (was sweeping - đang quét nhà) thì một hành động khác xen vào (arrived - đến).",
            "106": "Nhấn mạnh quá trình kéo dài 'for two days' xảy ra TRƯỚC một thời điểm trong quá khứ ('arrived'), ta dùng thì Quá khứ hoàn thành tiếp diễn (had been raining).",
            "107": "Động từ 'borrow' nghĩa là 'mượn (từ ai)'. Chủ ngữ 'He' ngôi thứ 3 số ít nên động từ thêm 's' thành 'borrows'. (Lend: cho mượn).",
            "108": "Giới từ 'before' chỉ thời gian trước một mốc cụ thể ('before six o'clock' - trước 6 giờ).",
            "109": "Cấu trúc 'look forward to + V-ing' (mong đợi làm việc gì đó).",
            "110": "Cấu trúc 'go + V-ing' chỉ các hoạt động thể thao, giải trí (go horseback riding - đi cưỡi ngựa)."
        },
        "translations": {
            "101": "Chiếc xe thuộc về chú tôi.",
            "102": "Cô ấy thỉnh thoảng ngáp trong lớp tiếng Anh.",
            "103": "Tôi thích xem phim hài trên TV.",
            "104": "Họ sẽ đến vào lúc 2 giờ ngày mai.",
            "105": "Khi tôi đến nhà dì tôi, bà ấy đang quét sàn bếp.",
            "106": "Trời đã mưa rả rích được hai ngày khi tôi đến thị trấn.",
            "107": "Anh ấy thỉnh thoảng mượn tiền từ bố mẹ.",
            "108": "Giao thông rất đông đúc, nhưng tôi nghĩ chúng ta sẽ đến đó trước sáu giờ.",
            "109": "Tất cả chúng tôi đều mong chờ được gặp bạn rất sớm.",
            "110": "Cuối tuần trước, chúng tôi đã đi cưỡi ngựa ở trang trại."
        }
    },
    "2": { "title": "Practice Test 2", "file": "reading_test_2.pdf", "answers": answers.get("2", {}), "explanations": {}, "translations": {} },
    "3": { "title": "Practice Test 3", "file": "reading_test_3.pdf", "answers": answers.get("3", {}), "explanations": {}, "translations": {} },
    "4": { "title": "Practice Test 4", "file": "reading_test_4.pdf", "answers": answers.get("4", {}), "explanations": {}, "translations": {} },
    "5": { "title": "Practice Test 5", "file": "reading_test_5.pdf", "answers": answers.get("5", {}), "explanations": {}, "translations": {} }
}

with open('reading_data.json', 'w', encoding='utf-8') as f:
    json.dump(test_data, f, ensure_ascii=False, indent=2)

print("Created full reading_data.json")
