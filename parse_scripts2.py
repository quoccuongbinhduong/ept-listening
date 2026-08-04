"""
Improved parser - builds structured questions with group_script for Parts 3 & 4
"""
import pdfplumber, json, re, os

SCRIPT_PATH = 'TAI LIEU EPT-TDMU SCRIPTS.pdf'

TEST_PAGE_RANGES = {
    1: (1, 7),
    2: (7, 14),
    3: (14, 21),
    4: (21, 28),
    5: (28, 35),
}

def reorder_2col(words, page_width):
    mid = page_width / 2
    lw = sorted([w for w in words if w['x0'] < mid],  key=lambda w: (round(w['top']/12)*12, w['x0']))
    rw = sorted([w for w in words if w['x0'] >= mid], key=lambda w: (round(w['top']/12)*12, w['x0']))
    return lw + rw

def words_to_lines(words):
    if not words: return []
    lines, cur = [], [words[0]]
    for w in words[1:]:
        if abs(w['top'] - cur[0]['top']) < 8:
            cur.append(w)
        else:
            lines.append(' '.join(x['text'] for x in sorted(cur, key=lambda x: x['x0'])))
            cur = [w]
    lines.append(' '.join(x['text'] for x in sorted(cur, key=lambda x: x['x0'])))
    return lines

OPTION_PAT = re.compile(r'^\(([ABCD])\)\s*(.*)')
QNUM_PAT   = re.compile(r'^(\d{1,3})\.\s*(.*)')
GROUP_PAT  = re.compile(r'Questions?\s+(\d+)[\s\-]+(?:through|and|to|-)*[\s\-]*(\d+)\s+refer', re.IGNORECASE)
PART_PAT   = re.compile(r'^PART\s+(\d+)', re.IGNORECASE)
SPEAKER_PAT = re.compile(r'^(Man|Woman|Narrator|Host|Speaker\s?\d*):', re.IGNORECASE)

def parse_questions(lines):
    questions  = {}
    cur_q      = None
    cur_group  = []        # lines of current group script
    group_range = []       # [start_q, end_q]
    in_header  = True
    part_num   = 0

    def flush_group():
        if group_range and cur_group:
            txt = '\n'.join(cur_group)
            for q in range(group_range[0], group_range[1]+1):
                if q not in questions:
                    questions[q] = {'text': '', 'options': {}}
                questions[q]['group_script'] = txt

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Skip empty
        if not line:
            i += 1
            continue

        # Part header
        pm = PART_PAT.match(line)
        if pm:
            part_num = int(pm.group(1))
            in_header = (part_num == 1)
            i += 1
            continue

        # "Practice Test N" header line
        if re.match(r'^Practice Test \d+', line):
            i += 1
            continue

        # Skip page numbers (just a number alone)
        if re.match(r'^\d+$', line) and len(line) <= 2:
            i += 1
            continue

        # Group reference: "Questions 41 through 43 refer to..."
        gm = GROUP_PAT.match(line)
        if gm:
            flush_group()
            q_start = int(gm.group(1))
            q_end   = int(gm.group(2))
            group_range = [q_start, q_end]
            cur_group = []
            # Collect header continuation on same or next line
            rest = line[gm.end():].strip()
            if rest:
                cur_group.append(rest)
            i += 1
            # Collect "following conversation/announcement/talk" line
            while i < len(lines):
                nxt = lines[i].strip()
                if not nxt:
                    i += 1
                    break
                if GROUP_PAT.match(nxt) or QNUM_PAT.match(nxt):
                    break
                cur_group.append(nxt)
                i += 1
            continue

        # Numbered question
        qm = QNUM_PAT.match(line)
        if qm:
            qnum = int(qm.group(1))
            if 1 <= qnum <= 100:
                cur_q = qnum
                q_text = qm.group(2).strip()
                if cur_q not in questions:
                    questions[cur_q] = {'text': q_text, 'options': {}, 'group_script': ''}
                else:
                    if q_text:
                        questions[cur_q]['text'] = q_text
                i += 1
                continue

        # Option (A)/(B)/(C)/(D)
        om = OPTION_PAT.match(line)
        if om and cur_q is not None:
            letter = om.group(1)
            txt = om.group(2).strip()
            # Check if next line continues this option
            j = i + 1
            while j < len(lines):
                nxt = lines[j].strip()
                if not nxt or OPTION_PAT.match(nxt) or QNUM_PAT.match(nxt) or GROUP_PAT.match(nxt):
                    break
                # Only continue if not a speaker line or part header
                if SPEAKER_PAT.match(nxt) or PART_PAT.match(nxt):
                    break
                txt += ' ' + nxt
                j += 1
            questions[cur_q]['options'][letter] = txt.strip()
            i = j
            continue

        # Speaker dialogue line (Man:, Woman:, etc.) -> part of group script
        if SPEAKER_PAT.match(line) or (cur_group is not None and group_range and
                                       cur_q is None and part_num >= 3):
            cur_group.append(line)
            i += 1
            continue

        # Continuation of group script (non-question lines after group header)
        if group_range and (cur_q is None or cur_q < group_range[0] or cur_q > group_range[1]):
            # We're between group header and first question of that group
            cur_group.append(line)
            i += 1
            continue

        i += 1

    flush_group()
    return questions

all_scripts = {}

with pdfplumber.open(SCRIPT_PATH) as pdf:
    total = len(pdf.pages)
    for test_num, (start_p, end_p) in TEST_PAGE_RANGES.items():
        lines = []
        for pi in range(start_p, min(end_p, total)):
            page = pdf.pages[pi]
            words = page.extract_words()
            if words:
                ordered = reorder_2col(words, page.width)
                lines.extend(words_to_lines(ordered))
        
        qs = parse_questions(lines)
        all_scripts[test_num] = qs
        
        # Stats
        with_opts  = sum(1 for q in qs.values() if q.get('options'))
        with_grp   = sum(1 for q in qs.values() if q.get('group_script'))
        print(f"Test {test_num}: {len(qs)} Qs, {with_opts} with options, {with_grp} with group script")
        
        # Sample Part 3
        for qn in [41, 42, 43, 71, 72]:
            if qn in qs:
                q = qs[qn]
                print(f"  Q{qn}: text='{q['text'][:50]}' opts={list(q['options'].keys())} grp={len(q.get('group_script',''))} chars")
                if q.get('group_script'):
                    print(f"    Script: {q['group_script'][:200]}")

# Save
scripts_json = {}
for t, qs in all_scripts.items():
    scripts_json[str(t)] = {}
    for qn, q in qs.items():
        scripts_json[str(t)][str(qn)] = {
            'text': q.get('text', ''),
            'options': q.get('options', {}),
            'group_script': q.get('group_script', ''),
        }

with open('scripts_structured.json', 'w', encoding='utf-8') as f:
    json.dump(scripts_json, f, ensure_ascii=False, indent=2)

print(f"\nSaved scripts_structured.json ({os.path.getsize('scripts_structured.json')//1024} KB)")
