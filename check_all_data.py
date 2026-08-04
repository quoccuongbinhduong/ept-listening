"""
Kiểm tra toàn diện dữ liệu cho 5 bài test:
- Part 1 (Q1-10): scripts có text + options A/B/C/D
- Part 2 (Q11-40): scripts có text + options A/B/C
- Part 3 (Q41-70): scripts có group_script + questions có q + o[4]
- Part 4 (Q71-100): scripts có group_script + questions có q + o[4]
"""
import json

scripts = json.load(open('scripts_structured.json', encoding='utf-8'))
answers = json.load(open('answers.json', encoding='utf-8'))

questions = {}
for fname in ['questions_1_2.json', 'questions_2.json', 'questions_4.json', 'questions_5.json']:
    try:
        data = json.load(open(fname, encoding='utf-8'))
        for t in data:
            if t not in questions:
                questions[t] = data[t]
            else:
                questions[t].update(data[t])
    except FileNotFoundError:
        pass

PARTS = {
    1: (1, 10,  ['A','B','C','D']),
    2: (11, 40, ['A','B','C']),
    3: (41, 70, ['A','B','C','D']),
    4: (71, 100, ['A','B','C','D']),
}

print("="*70)
print("KIỂM TRA DỮ LIỆU CHO 5 BÀI TEST")
print("="*70)

all_ok = True
for test in ['1','2','3','4','5']:
    print(f"\n{'='*40}")
    print(f"PRACTICE TEST {test}")
    print(f"{'='*40}")
    
    test_scripts = scripts.get(test, {})
    test_questions = questions.get(test, {})
    test_answers = answers.get(test, {})
    
    for part_id, (start, end, opts) in PARTS.items():
        issues = []
        ok_count = 0
        
        for q in range(start, end + 1):
            qstr = str(q)
            sd = test_scripts.get(qstr, {})
            qd = test_questions.get(qstr, {})
            
            q_issues = []
            
            if part_id in [1, 2]:
                # Parts 1&2: need text + options in scripts
                if not sd.get('text'):
                    q_issues.append('no text')
                for letter in opts:
                    if not sd.get('options', {}).get(letter):
                        q_issues.append(f'no opt {letter}')
                        
            elif part_id in [3, 4]:
                # Parts 3&4: need group_script + question text + 4 options
                if not sd.get('group_script') or len(sd.get('group_script','')) < 20:
                    q_issues.append('no/short group_script')
                # Question text (from questions JSON)
                if not qd.get('q'):
                    q_issues.append('no question text')
                # Options (from questions JSON)
                if not qd.get('o') or len(qd.get('o', [])) < 4:
                    q_issues.append(f"options: {len(qd.get('o',[]))} (need 4)")
                elif qd['o'][0] == '':
                    q_issues.append('empty option A')
                # Fallback: check script options
                elif not qd.get('q') and not sd.get('options', {}).get('A'):
                    q_issues.append('no options anywhere')
            
            # Check answer exists
            if not test_answers.get(qstr):
                q_issues.append('no answer key')
            
            if q_issues:
                issues.append((q, q_issues))
            else:
                ok_count += 1
        
        total = end - start + 1
        if issues:
            all_ok = False
            print(f"  Part {part_id} (Q{start}-{end}): {ok_count}/{total} ✅  {total-ok_count} ❌")
            # Show first 5 issues
            for q, qi in issues[:5]:
                print(f"    Q{q}: {', '.join(qi)}")
            if len(issues) > 5:
                print(f"    ... và {len(issues)-5} câu khác")
        else:
            print(f"  Part {part_id} (Q{start}-{end}): {ok_count}/{total} ✅  TẤT CẢ HOÀN CHỈNH")

print(f"\n{'='*70}")
if all_ok:
    print("✅ TẤT CẢ 5 BÀI TEST ĐÃ HOÀN CHỈNH!")
else:
    print("❌ CÒN MỘT SỐ VẤN ĐỀ CẦN SỬA")
print("="*70)
