import json

with open('D:/EPT/ept-deploy/test5_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

explanations = {}
for q in data:
    qn = str(q['qn'])
    ans = q.get('correct_answer', '')
    part = q.get('part', 1)
    
    options = q.get('options', {})
    opt_text = options.get(ans, '')
    
    if part == 1:
        expl = f"Đáp án {ans} đúng vì lựa chọn '{opt_text}' mô tả chính xác nhất nội dung bức tranh."
    elif part == 2:
        expl = f"Đáp án {ans} đúng vì '{opt_text}' là phản hồi tự nhiên và phù hợp nhất cho câu hỏi."
    else:
        expl = f"Đáp án {ans} đúng vì thông tin '{opt_text}' khớp với nội dung được nhắc đến trong đoạn băng."
        
    explanations[qn] = expl

with open('D:/EPT/ept-deploy/final_explanations_5.json', 'w', encoding='utf-8') as f:
    json.dump(explanations, f, ensure_ascii=False, indent=4)

print('Done')
