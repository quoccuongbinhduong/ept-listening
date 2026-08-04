import pdfplumber, json, re

def parse_script_questions(script_text, test_num):
    questions = {}
    
    # Split by part headers
    part_pattern = re.compile(r'PART\s+(\d+)[:\s]+(PHOTOS|QUESTION-RESPONSE|CONVERSATIONS|TALKS?)', re.IGNORECASE)
    
    # Find part boundaries
    part_matches = list(part_pattern.finditer(script_text))
    
    for idx, match in enumerate(part_matches):
        part_num = int(match.group(1))
        part_name = match.group(2).upper()
        
        start = match.end()
        end = part_matches[idx+1].start() if idx+1 < len(part_matches) else len(script_text)
        part_content = script_text[start:end]
        
        # Find individual questions with options
        # Each question like: "11. When did the director arrive?\n(A) ...\n(B) ...\n(C) ..."
        q_blocks = re.split(r'\n(\d+)\.\s+', part_content)
        
        i = 1
        while i < len(q_blocks) - 1:
            q_num_str = q_blocks[i]
            q_body = q_blocks[i+1] if i+1 < len(q_blocks) else ''
            
            try:
                q_num = int(q_num_str)
            except:
                i += 2
                continue
            
            if q_num < 1 or q_num > 100:
                i += 2
                continue
            
            # Extract main text and options
            # Find options (A), (B), (C), (D)
            lines = q_body.strip().split('\n')
            main_lines = []
            options = {}
            opt_pattern = re.compile(r'^\(([ABCD])\)\s*(.*)')
            
            for line in lines:
                m = opt_pattern.match(line.strip())
                if m:
                    options[m.group(1)] = m.group(2).strip()
                else:
                    if not options:  # still in main text
                        main_lines.append(line.strip())
            
            main_text = ' '.join(l for l in main_lines if l).strip()
            
            questions[q_num] = {
                'part': part_num,
                'part_name': part_name,
                'text': main_text,
                'options': options
            }
            
            i += 2
    
    return questions

# Load existing data
with open('ept_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Parse and display for test 1
script1 = data['scripts']['1']
qs = parse_script_questions(script1, 1)
print(f'Test 1: {len(qs)} questions parsed')

for qn in sorted(qs.keys())[:20]:
    q = qs[qn]
    print(f"Q{qn} (Part {q['part']} - {q['part_name']}): {q['text'][:70]}")
    for k, v in q['options'].items():
        print(f"  ({k}) {v[:50]}")
    print()
