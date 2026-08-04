"""
Generate Vietnamese explanations for all 5 tests x 100 questions.
- Part 1 (q1-10): Photo description - uses option text
- Part 2 (q11-40): Question-Response - uses Q+A text  
- Part 3 (q41-70): Conversations - extracts relevant quote from group_script
- Part 4 (q71-100): Talks - extracts relevant quote from group_script

Output: explanations.json  -> {"1": {"1": "...", "2": "..."}, ...}
"""
import json
import re

with open('core_for_expl.json', 'r', encoding='utf-8') as f:
    core = json.load(f)

answers = core['answers']
scripts = core['scripts']
questions = core['questions']

def find_relevant_sentence(script_text, correct_option_text):
    """Find sentence in script that best matches the correct option."""
    if not script_text or not correct_option_text:
        return ""
    
    # Split script into sentences
    sentences = re.split(r'(?<=[.!?])\s+', script_text.strip())
    
    # Get keywords from correct option (remove common words)
    stop_words = {'the','a','an','is','are','was','were','to','of','in','on','at',
                  'he','she','it','we','they','i','you','his','her','its','our','their',
                  'be','will','can','do','does','did','have','has','had','not','no'}
    
    opt_words = set(w.lower().strip('.,!?') for w in correct_option_text.split() 
                   if w.lower().strip('.,!?') not in stop_words and len(w) > 2)
    
    # Score each sentence
    best_score = 0
    best_sentence = ""
    
    for sent in sentences:
        sent_words = set(w.lower().strip('.,!?') for w in sent.split())
        score = len(opt_words & sent_words)
        if score > best_score:
            best_score = score
            best_sentence = sent.strip()
    
    return best_sentence if best_score >= 1 else ""


def make_explanation(test_str, q_str, answers_data, scripts_data, questions_data):
    """Generate explanation for a single question."""
    qn = int(q_str)
    ca = answers_data.get(q_str, '')  # correct answer letter
    
    sd = scripts_data.get(q_str, {})
    qd = questions_data.get(q_str, {})
    
    script_opts = sd.get('options', {})
    correct_opt_text = script_opts.get(ca, '')
    group_script = sd.get('group_script', '') or ''
    script_text = sd.get('text', '') or ''
    
    # Question text
    q_text = ''
    if qd and qd.get('q'):
        q_text = qd['q']
    elif script_text:
        q_text = script_text
    
    # Options from questions data (more complete)
    q_opts = qd.get('o', []) if qd else []
    opt_letters = ['A','B','C','D']
    
    # Build option text map
    opt_map = {}
    if q_opts:
        for i, letter in enumerate(opt_letters):
            if i < len(q_opts):
                opt_map[letter] = q_opts[i]
    
    # Use script_opts as fallback
    for letter in opt_letters:
        if letter not in opt_map and letter in script_opts:
            opt_map[letter] = script_opts[letter]
    
    correct_text = opt_map.get(ca, correct_opt_text)
    
    # ── Part 1: Photos (q1-10) ──
    if qn <= 10:
        opts_display = ""
        for letter in ['A','B','C','D']:
            t = opt_map.get(letter, script_opts.get(letter, ''))
            if t:
                marker = "✓" if letter == ca else "✗"
                opts_display += f"{marker} {letter}. {t}\n"
        
        return (
            f"Đây là câu hỏi mô tả hình ảnh (Part 1).\n"
            f"Đáp án đúng là **{ca}**: \"{correct_text}\"\n\n"
            f"Lựa chọn này mô tả chính xác nhất nội dung của bức tranh."
        )
    
    # ── Part 2: Question-Response (q11-40) ──
    elif qn <= 40:
        q_display = q_text if q_text else "..."
        opts_str = ""
        for letter in ['A','B','C']:
            t = opt_map.get(letter, script_opts.get(letter, ''))
            if t:
                marker = "✓" if letter == ca else " "
                opts_str += f"{marker} {letter}. {t}\n"
        
        reason = ""
        if ca == 'A':
            wrong = ['B', 'C']
        elif ca == 'B':
            wrong = ['A', 'C']
        else:
            wrong = ['A', 'B']
        
        wrong_reasons = []
        for w in wrong:
            wt = opt_map.get(w, script_opts.get(w, ''))
            if wt:
                wrong_reasons.append(f"{w}. \"{wt}\"")
        
        reason_text = ""
        if wrong_reasons:
            reason_text = f"\nCác đáp án còn lại ({', '.join(wrong_reasons)}) không phù hợp với ngữ cảnh câu hỏi."
        
        return (
            f"Đây là câu hỏi phản hồi ngắn (Part 2).\n"
            f"Câu hỏi/phát biểu: \"{q_display}\"\n\n"
            f"Đáp án đúng là **{ca}**: \"{correct_text}\"\n"
            f"Đây là phản hồi phù hợp và tự nhiên nhất với câu hỏi trên.{reason_text}"
        )
    
    # ── Part 3 & 4: Conversations & Talks (q41-100) ──
    else:
        q_display = q_text if q_text else f"Câu {qn}"
        
        # Find relevant quote from group_script
        relevant_quote = find_relevant_sentence(group_script, correct_text)
        
        quote_line = ""
        if relevant_quote:
            # Clean up speaker labels
            clean_quote = re.sub(r'^(Man|Woman|Narrator|Host|Speaker\s*\d*):\s*', '', relevant_quote, flags=re.IGNORECASE)
            quote_line = f"\nCâu chốt trong đoạn băng: \"{clean_quote}\""
        
        return (
            f"Câu hỏi: \"{q_display}\"\n"
            f"Đáp án đúng là **{ca}**: \"{correct_text}\"{quote_line}\n\n"
            f"Thông tin này được đề cập trực tiếp trong đoạn hội thoại/bài nói."
        )


# Generate all explanations
all_explanations = {}
total = 0
for test_str in ['1','2','3','4','5']:
    all_explanations[test_str] = {}
    test_answers = answers.get(test_str, {})
    test_scripts = scripts.get(test_str, {})
    test_questions = questions.get(test_str, {})
    
    for q_str in [str(i) for i in range(1, 101)]:
        if q_str not in test_answers:
            continue
        try:
            expl = make_explanation(test_str, q_str, test_answers, test_scripts, test_questions)
            all_explanations[test_str][q_str] = expl
            total += 1
        except Exception as e:
            print(f"Error Test {test_str} Q{q_str}: {e}")
            all_explanations[test_str][q_str] = f"Đáp án đúng là {test_answers.get(q_str, '?')}."

print(f"Generated {total} explanations")

with open('explanations.json', 'w', encoding='utf-8') as f:
    json.dump(all_explanations, f, ensure_ascii=False, indent=2)

print("Saved explanations.json")

# Sample a few
for test_str in ['1','2','3']:
    for q_str in ['5','15','45','75']:
        expl = all_explanations.get(test_str, {}).get(q_str, '')
        if expl:
            print(f"\n--- Test {test_str} Q{q_str} ---")
            print(expl[:300])
