import json
import re
import time
import os

try:
    from deep_translator import GoogleTranslator
    translator = GoogleTranslator(source='en', target='vi')
    def translate_en_vi(text):
        if not text: return ""
        try:
            time.sleep(0.1)
            return translator.translate(text)
        except Exception as e:
            print("Lỗi dịch:", e)
            return "(Lỗi dịch)"
except ImportError:
    def translate_en_vi(text):
        return "(Bản dịch đang cập nhật - thiếu thư viện)"

with open('core_for_expl.json', 'r', encoding='utf-8') as f:
    core = json.load(f)

answers = core['answers']
scripts = core['scripts']
questions = core['questions']

cache_file = "translation_cache.json"
if os.path.exists(cache_file):
    with open(cache_file, 'r', encoding='utf-8') as f:
        t_cache = json.load(f)
else:
    t_cache = {}

def get_trans(text):
    if not text: return ""
    text = text.strip()
    if text in t_cache:
        return t_cache[text]
    tv = translate_en_vi(text)
    t_cache[text] = tv
    return tv

def find_relevant_sentence(script_text, correct_option_text):
    if not script_text or not correct_option_text:
        return ""
    sentences = re.split(r'(?<=[.!?])\s+', script_text.strip())
    stop_words = {'the','a','an','is','are','was','were','to','of','in','on','at',
                  'he','she','it','we','they','i','you','his','her','its','our','their',
                  'be','will','can','do','does','did','have','has','had','not','no'}
    opt_words = set(w.lower().strip('.,!?') for w in correct_option_text.split() 
                   if w.lower().strip('.,!?') not in stop_words and len(w) > 2)
    best_score = 0
    best_sentence = ""
    for sent in sentences:
        sent_words = set(w.lower().strip('.,!?') for w in sent.split())
        score = len(opt_words & sent_words)
        if score > best_score:
            best_score = score
            best_sentence = sent.strip()
    return best_sentence if best_score >= 1 else ""

all_explanations = {}
for test_str in ['1','2','3','4','5']:
    all_explanations[test_str] = {}
    test_answers = answers.get(test_str, {})
    test_scripts = scripts.get(test_str, {})
    test_questions = questions.get(test_str, {})
    
    print(f"Processing Test {test_str}...")
    for q_str in [str(i) for i in range(1, 101)]:
        if q_str not in test_answers:
            continue
        qn = int(q_str)
        ca = test_answers.get(q_str, '')
        sd = test_scripts.get(q_str, {})
        qd = test_questions.get(q_str, {})
        
        script_opts = sd.get('options', {})
        correct_opt_text = script_opts.get(ca, '')
        group_script = sd.get('group_script', '') or ''
        script_text = sd.get('text', '') or ''
        
        q_text = qd.get('q') if qd and qd.get('q') else script_text
        q_opts = qd.get('o', []) if qd else []
        opt_map = {}
        opt_letters = ['A','B','C','D']
        if q_opts:
            for i, letter in enumerate(opt_letters):
                if i < len(q_opts):
                    opt_map[letter] = q_opts[i]
        for letter in opt_letters:
            if letter not in opt_map and letter in script_opts:
                opt_map[letter] = script_opts[letter]
        
        correct_text = opt_map.get(ca, correct_opt_text)
        
        # Part 1
        if qn <= 10:
            wrong_opts = ""
            for letter in ['A','B','C','D']:
                if letter != ca:
                    t = opt_map.get(letter, script_opts.get(letter, ''))
                    if t:
                        tv = get_trans(t)
                        wrong_opts += f"  ✗ {letter}. \"{t}\"\n      → {tv}\n"
            
            c_trans = get_trans(correct_text)
            expl = (
                f"✦ Câu hỏi: Nghe mô tả và chọn câu đúng nhất cho hình.\n"
                f"📌 Đáp án đúng: {ca} – \"{correct_text}\"\n"
                f"   → Dịch: \"{c_trans}\"\n\n"
                f"Tại sao đúng: Đây là mô tả phù hợp nhất với hành động/chi tiết trong ảnh.\n"
                f"Tại sao sai:\n{wrong_opts}"
            )
            
        # Part 2
        elif qn <= 40:
            q_display = q_text if q_text else "..."
            q_trans = get_trans(q_display)
            c_trans = get_trans(correct_text)
            
            wrong_opts = ""
            for letter in ['A','B','C']:
                if letter != ca:
                    t = opt_map.get(letter, script_opts.get(letter, ''))
                    if t:
                        tv = get_trans(t)
                        wrong_opts += f"  ✗ {letter}. \"{t}\"\n      → \"{tv}\" (không phù hợp ngữ cảnh)\n"
                        
            expl = (
                f"🎧 Câu hỏi: \"{q_display}\"\n"
                f"   → Dịch: \"{q_trans}\"\n\n"
                f"📌 Đáp án đúng: {ca} – \"{correct_text}\"\n"
                f"   → Dịch: \"{c_trans}\"\n"
                f"   → Lý do: Đây là câu trả lời trực tiếp và phù hợp nhất cho câu hỏi trên.\n\n"
                f"Tại sao sai:\n{wrong_opts}"
            )
            
        # Part 3 & 4
        else:
            q_display = q_text if q_text else f"Câu {qn}"
            q_trans = get_trans(q_display)
            c_trans = get_trans(correct_text)
            
            relevant_quote = find_relevant_sentence(group_script, correct_text)
            quote_line = ""
            if relevant_quote:
                clean_quote = re.sub(r'^(Man|Woman|Narrator|Host|Speaker\s*\d*):\s*', '', relevant_quote, flags=re.IGNORECASE)
                clean_trans = get_trans(clean_quote)
                quote_line = f"\n🎙️ Câu chốt trong đoạn băng: \"{clean_quote}\"\n   → Dịch: \"{clean_trans}\"\n"
            
            expl = (
                f"❓ Câu hỏi: \"{q_display}\"\n"
                f"   → Dịch: \"{q_trans}\"\n\n"
                f"📌 Đáp án đúng: {ca} – \"{correct_text}\"\n"
                f"   → Dịch: \"{c_trans}\"\n"
                f"{quote_line}\n"
                f"💡 Lý do: Thông tin được đề cập trực tiếp trong đoạn hội thoại/bài nói."
            )
            
        all_explanations[test_str][q_str] = expl
        
    with open(cache_file, 'w', encoding='utf-8') as f:
        json.dump(t_cache, f, ensure_ascii=False)
        
with open('explanations.json', 'w', encoding='utf-8') as f:
    json.dump(all_explanations, f, ensure_ascii=False, indent=2)

print("Đã tạo xong explanations.json với format mới!")
