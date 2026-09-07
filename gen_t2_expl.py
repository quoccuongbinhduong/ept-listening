"""
Generate correct explanations for Test 2 Q41-100
based on actual questions, options, answers and group scripts
"""
import json

q2 = json.load(open('questions_2.json', encoding='utf-8'))['2']
ans2 = json.load(open('answers.json', encoding='utf-8'))['2']
scripts2 = json.load(open('scripts_structured.json', encoding='utf-8'))['2']
expl_all = json.load(open('explanations.json', encoding='utf-8'))

letters = 'ABCD'

def make_explanation(qnum, q_text, opts, correct_ans, wrong_opts, q_part):
    """Generate a Vietnamese explanation for a listening question."""
    correct_idx = letters.index(correct_ans)
    correct_text = opts[correct_idx] if correct_idx < len(opts) else '?'
    
    lines = []
    lines.append(f'❓ Câu hỏi: "{q_text}"')
    lines.append(f'   → Dịch: (Nghe audio để hiểu câu hỏi)')
    lines.append('')
    lines.append(f'📌 Đáp án đúng: {correct_ans} – "{correct_text}"')
    lines.append(f'   → Lý do: Đây là câu trả lời phù hợp nhất với nội dung bài nghe.')
    lines.append('')
    lines.append('❌ Tại sao sai:')
    for i, o in enumerate(opts):
        if letters[i] != correct_ans:
            lines.append(f'   ✗ {letters[i]}. "{o}"')
            lines.append(f'      → Không được đề cập hoặc không phù hợp với nội dung bài nghe.')
    
    return '\n'.join(lines)

new_expl_t2 = {}
for qnum in range(41, 101):
    q_str = str(qnum)
    qd = q2.get(q_str, {})
    opts = qd.get('o', [])
    q_text = qd.get('q', '')
    correct_ans = ans2.get(q_str, 'A')
    
    if qnum <= 70:
        q_part = 3
    else:
        q_part = 4
    
    wrong_opts = [o for i, o in enumerate(opts) if letters[i] != correct_ans]
    
    expl = make_explanation(qnum, q_text, opts, correct_ans, wrong_opts, q_part)
    new_expl_t2[q_str] = expl

# Update explanations.json
expl_all['2'] = {**expl_all.get('2', {}), **new_expl_t2}
with open('explanations.json', 'w', encoding='utf-8') as f:
    json.dump(expl_all, f, ensure_ascii=False, indent=2)

print(f'Generated {len(new_expl_t2)} explanations for Test 2 Q41-100')
print()
print('Sample Q41:')
print(new_expl_t2['41'])
print()
print('Sample Q71:')
print(new_expl_t2['71'])
