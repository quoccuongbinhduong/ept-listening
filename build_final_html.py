"""
Build final index.html embedding:
- Photos (base64) for Part 1 Test 1
- Script options for all tests (Parts 1 & 2: 40 questions with A/B/C/D)
- Group scripts for Parts 3 & 4
- All answer keys
"""
import json, os, re, pdfplumber, fitz, base64
from PIL import Image
from io import BytesIO

# ── Load existing data ──────────────────────────────────────
with open('scripts_structured.json', encoding='utf-8') as f:
    scripts_json = json.load(f)

# ── Re-extract answers ──────────────────────────────────────
answers = {}
with pdfplumber.open('TAI LIEU EPT-TDMU Đáp án.pdf') as pdf:
    current_test = None; in_listening = True
    for page in pdf.pages:
        text = page.extract_text()
        if not text: continue
        for line in text.split('\n'):
            if 'A. LISTENING' in line: in_listening = True; continue
            if 'B. READING'   in line: in_listening = False; continue
            m = re.match(r'Practice Test (\d+)', line.strip())
            if m:
                current_test = int(m.group(1))
                if in_listening and current_test not in answers:
                    answers[current_test] = {}
                continue
            if current_test and in_listening:
                for num, ans in re.findall(r'(\d+)\s+([ABCD])', line):
                    n = int(num)
                    if n <= 100: answers[current_test][n] = ans

answers_json = {str(t): {str(k): v for k,v in ans.items()} for t,ans in answers.items()}

# ── Extract Part-1 photos ───────────────────────────────────
print("Extracting photos...")
doc = fitz.open('LISTENING PRACTICE-1.pdf')
photos_b64 = {}
PHOTO_PAGES = {2:(1,2), 3:(3,4), 4:(5,6), 5:(7,8), 6:(9,10)}
for page_num, (q1, q2) in PHOTO_PAGES.items():
    page = doc[page_num-1]
    mat  = fitz.Matrix(1.8, 1.8)
    pix  = page.get_pixmap(matrix=mat, alpha=False)
    img  = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    W, H = img.width, img.height
    pad  = 12
    mid  = H // 2
    for qn, crop in [(q1, img.crop((pad, int(H*.02), W-pad, mid-pad))),
                     (q2, img.crop((pad, mid+pad, W-pad, H-int(H*.02))))]:
        buf = BytesIO()
        crop.save(buf, format='JPEG', quality=78)
        photos_b64[str(qn)] = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
        print(f"  Q{qn}: {crop.size}")

print(f"Photos: {len(photos_b64)}")
print("Building HTML...")

# ── JSON payload for embedding ──────────────────────────────
payload = json.dumps({
    'answers': answers_json,
    'scripts': scripts_json,
    'photos':  photos_b64,
}, ensure_ascii=False, separators=(',',':'))

print(f"Payload size: {len(payload)//1024} KB")

# ── HTML template ───────────────────────────────────────────
HTML = r"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0"/>
  <title>EPT Listening Practice – TDMU</title>
  <meta name="description" content="Luyện nghe EPT-TDMU: 5 bài Practice Test, đáp án chi tiết, script và hình ảnh."/>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"/>
  <style>
:root{
  --bg:#0d0f1a;--surface:#151828;--surface2:#1e2235;--border:#2a2f4a;
  --accent:#6c63ff;--accent2:#a78bfa;
  --green:#22c55e;--red:#ef4444;--yellow:#facc15;--orange:#f97316;
  --text:#e2e8f0;--muted:#8892a4;--radius:14px;--shadow:0 4px 24px rgba(0,0,0,.45);
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;}
body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--text);min-height:100vh;overflow-x:hidden;}
body::before{content:'';position:fixed;inset:0;z-index:-1;background:
  radial-gradient(ellipse 80% 60% at 20% 20%,rgba(108,99,255,.15) 0%,transparent 60%),
  radial-gradient(ellipse 60% 80% at 80% 80%,rgba(167,139,250,.10) 0%,transparent 60%);}

/* ── HEADER */
header{background:rgba(21,24,40,.9);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);
  padding:12px 18px;position:sticky;top:0;z-index:100;display:flex;align-items:center;gap:12px;}
.logo-icon{width:38px;height:38px;background:linear-gradient(135deg,var(--accent),var(--accent2));
  border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0;}
.logo-text h1{font-size:15px;font-weight:700;}
.logo-text p{font-size:11px;color:var(--muted);}

/* ── CONTAINER */
.container{max-width:860px;margin:0 auto;padding:18px 14px 100px;}

/* ── ANIMATIONS */
@keyframes fadeUp{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}
@keyframes pulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.5;transform:scale(1.3)}}

/* ── HOME */
#screen-home{animation:fadeUp .4s ease;}
.home-hero{text-align:center;padding:36px 0 28px;}
.hero-badge{display:inline-block;background:rgba(108,99,255,.2);border:1px solid rgba(108,99,255,.4);
  color:var(--accent2);font-size:11px;font-weight:600;padding:3px 12px;border-radius:999px;margin-bottom:14px;}
.home-hero h2{font-size:clamp(22px,5vw,34px);font-weight:800;
  background:linear-gradient(135deg,#fff 0%,var(--accent2) 100%);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:8px;}
.home-hero p{color:var(--muted);font-size:14px;line-height:1.6;}
.stats-row{display:flex;gap:10px;flex-wrap:wrap;justify-content:center;margin:20px 0;}
.stat-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);
  padding:14px 20px;text-align:center;flex:1;min-width:110px;}
.stat-card .num{font-size:26px;font-weight:800;color:var(--accent2);}
.stat-card .lbl{font-size:11px;color:var(--muted);margin-top:2px;}
.section-title{font-size:12px;font-weight:600;color:var(--muted);text-transform:uppercase;
  letter-spacing:1px;margin:24px 0 10px;}
.test-grid{display:grid;gap:10px;}
.test-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);
  padding:16px 18px;cursor:pointer;display:flex;align-items:center;gap:14px;
  transition:all .2s;position:relative;overflow:hidden;}
.test-card::before{content:'';position:absolute;left:0;top:0;bottom:0;width:3px;
  background:linear-gradient(to bottom,var(--accent),var(--accent2));border-radius:3px 0 0 3px;}
.test-card:hover{border-color:var(--accent);transform:translateY(-2px);box-shadow:0 8px 28px rgba(108,99,255,.2);}
.test-num{width:46px;height:46px;flex-shrink:0;background:linear-gradient(135deg,var(--accent),var(--accent2));
  border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:17px;font-weight:800;}
.test-info .name{font-weight:600;font-size:14px;margin-bottom:3px;}
.test-info .meta{font-size:11px;color:var(--muted);display:flex;gap:10px;flex-wrap:wrap;}
.test-info .meta span{display:flex;align-items:center;gap:3px;}
.test-arrow{color:var(--muted);font-size:18px;margin-left:auto;}
.test-progress{height:3px;background:var(--border);border-radius:2px;margin-top:8px;overflow:hidden;}
.test-progress-fill{height:100%;background:linear-gradient(to right,var(--accent),var(--accent2));transition:width .5s;}
.part-info-box{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);
  padding:14px 16px;font-size:13px;line-height:2.1;color:var(--muted);}

/* ── EXAM */
#screen-exam{display:none;animation:fadeUp .3s ease;}
.exam-toolbar{display:flex;align-items:center;gap:10px;margin-bottom:14px;flex-wrap:wrap;}
.btn-back{background:var(--surface2);border:1px solid var(--border);color:var(--text);
  border-radius:10px;padding:7px 12px;cursor:pointer;font-size:12px;font-weight:500;
  display:flex;align-items:center;gap:5px;transition:all .2s;}
.btn-back:hover{border-color:var(--accent);}
.exam-title{font-weight:700;font-size:15px;flex:1;}
.score-badge{background:var(--surface2);border:1px solid var(--border);border-radius:10px;
  padding:7px 14px;font-size:12px;font-weight:600;}
.score-badge span{color:var(--accent2);}

/* ── AUDIO PLAYER */
.audio-panel{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);
  padding:18px;margin-bottom:16px;}
.audio-label{font-size:11px;color:var(--muted);font-weight:600;text-transform:uppercase;
  letter-spacing:1px;margin-bottom:12px;display:flex;align-items:center;gap:8px;}
.audio-label::before{content:'';width:8px;height:8px;background:var(--green);border-radius:50%;animation:pulse 1.5s infinite;}
.player-wrap{display:flex;flex-direction:column;gap:10px;}
.player-controls{display:flex;align-items:center;gap:10px;}
.btn-play{width:48px;height:48px;flex-shrink:0;border-radius:50%;
  background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;cursor:pointer;
  color:#fff;font-size:18px;display:flex;align-items:center;justify-content:center;
  box-shadow:0 4px 18px rgba(108,99,255,.5);transition:transform .15s,box-shadow .15s;}
.btn-play:hover{transform:scale(1.08);box-shadow:0 6px 26px rgba(108,99,255,.7);}
.btn-play:active{transform:scale(.95);}
.player-time-wrap{flex:1;}
.player-seek{width:100%;height:5px;-webkit-appearance:none;appearance:none;
  background:var(--border);border-radius:3px;cursor:pointer;outline:none;}
.player-seek::-webkit-slider-thumb{-webkit-appearance:none;width:15px;height:15px;
  background:var(--accent2);border-radius:50%;cursor:pointer;box-shadow:0 0 8px rgba(167,139,250,.6);}
.player-time{display:flex;justify-content:space-between;font-size:10px;color:var(--muted);margin-top:4px;}
.speed-row{display:flex;gap:5px;flex-wrap:wrap;align-items:center;}
.speed-row span{font-size:11px;color:var(--muted);}
.speed-btn{background:var(--surface2);border:1px solid var(--border);color:var(--text);
  border-radius:7px;padding:4px 10px;cursor:pointer;font-size:11px;font-weight:600;transition:all .2s;}
.speed-btn:hover{border-color:var(--accent);color:var(--accent2);}
.speed-btn.active{background:rgba(108,99,255,.2);border-color:var(--accent);color:var(--accent2);}

/* ── PARTS NAV */
.parts-nav{display:flex;gap:6px;margin-bottom:14px;flex-wrap:wrap;}
.part-tab{padding:6px 12px;border-radius:7px;cursor:pointer;font-size:11px;font-weight:600;
  background:var(--surface2);border:1px solid var(--border);transition:all .2s;white-space:nowrap;}
.part-tab:hover{border-color:var(--accent);}
.part-tab.active{background:rgba(108,99,255,.25);border-color:var(--accent);color:var(--accent2);}

/* ── QUESTION MAP */
.q-map-wrap{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:12px;margin-bottom:14px;}
.q-map-title{font-size:11px;color:var(--muted);font-weight:600;margin-bottom:8px;display:flex;justify-content:space-between;}
.question-map{display:grid;grid-template-columns:repeat(auto-fill,minmax(34px,1fr));gap:4px;}
.q-dot{height:34px;width:100%;border-radius:6px;cursor:pointer;font-size:11px;font-weight:700;
  display:flex;align-items:center;justify-content:center;background:var(--surface2);
  border:1px solid var(--border);transition:all .12s;color:var(--muted);}
.q-dot:hover{border-color:var(--accent);color:var(--text);}
.q-dot.answered{background:rgba(108,99,255,.2);border-color:var(--accent);color:var(--accent2);}
.q-dot.correct{background:rgba(34,197,94,.2);border-color:var(--green);color:var(--green);}
.q-dot.wrong{background:rgba(239,68,68,.2);border-color:var(--red);color:var(--red);}
.q-dot.current{background:var(--accent);border-color:var(--accent);color:#fff;transform:scale(1.1);}

/* ── QUESTION PANEL */
.question-panel{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);
  padding:18px;margin-bottom:14px;animation:fadeUp .25s ease;}
.q-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px;}
.q-number{font-size:12px;color:var(--muted);font-weight:600;}
.q-part-badge{font-size:10px;font-weight:600;background:rgba(108,99,255,.2);color:var(--accent2);
  padding:3px 10px;border-radius:999px;}

/* ── PHOTO */
.photo-wrap{margin-bottom:14px;border-radius:12px;overflow:hidden;border:1px solid var(--border);}
.photo-wrap img{width:100%;display:block;border-radius:12px;}
.photo-label{font-size:11px;color:var(--muted);text-align:center;padding:6px;
  background:var(--surface2);}

/* ── QUESTION TEXT */
.q-text{font-size:14px;line-height:1.6;color:var(--text);margin-bottom:14px;padding:12px;
  background:var(--surface2);border-radius:10px;border-left:3px solid var(--accent);}
.q-text.hidden{display:none;}

/* ── OPTIONS */
.options-list{display:flex;flex-direction:column;gap:8px;}
.option-btn{display:flex;align-items:center;gap:12px;padding:12px 14px;
  background:var(--surface2);border:1.5px solid var(--border);border-radius:11px;
  cursor:pointer;text-align:left;width:100%;transition:all .18s;font-size:13px;color:var(--text);}
.option-btn:hover{border-color:var(--accent);background:rgba(108,99,255,.08);transform:translateX(3px);}
.option-btn.selected{border-color:var(--accent);background:rgba(108,99,255,.18);color:#fff;}
.option-btn.correct{border-color:var(--green);background:rgba(34,197,94,.15);color:var(--green);}
.option-btn.wrong{border-color:var(--red);background:rgba(239,68,68,.15);color:var(--red);}
.option-btn:disabled{cursor:default;transform:none!important;}
.opt-letter{width:30px;height:30px;flex-shrink:0;border-radius:50%;background:rgba(255,255,255,.08);
  display:flex;align-items:center;justify-content:center;font-weight:700;font-size:13px;transition:background .18s;}
.option-btn.selected .opt-letter{background:var(--accent);color:#fff;}
.option-btn.correct .opt-letter{background:var(--green);color:#fff;}
.option-btn.wrong   .opt-letter{background:var(--red);color:#fff;}
.opt-text{flex:1;line-height:1.5;}

/* ── GROUP SCRIPT */
.group-script-box{background:rgba(108,99,255,.06);border:1px solid rgba(108,99,255,.25);
  border-radius:12px;padding:14px 16px;margin-bottom:14px;}
.gs-title{font-size:11px;font-weight:600;color:var(--accent2);text-transform:uppercase;
  letter-spacing:.5px;margin-bottom:10px;display:flex;align-items:center;gap:6px;}
.gs-body{font-size:13px;line-height:1.85;color:var(--text);white-space:pre-wrap;}
.gs-line-speaker{color:var(--accent2);font-weight:600;}
.gs-line-content{color:var(--text);}

/* ── Q NAV */
.q-nav{display:flex;gap:8px;margin-top:14px;flex-wrap:wrap;}
.btn-nav{flex:1;padding:11px;border-radius:11px;border:1px solid var(--border);
  background:var(--surface2);color:var(--text);cursor:pointer;font-size:13px;font-weight:600;transition:all .2s;}
.btn-nav:hover{border-color:var(--accent);}
.btn-nav.primary{background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;color:#fff;
  box-shadow:0 4px 14px rgba(108,99,255,.4);}
.btn-nav.primary:hover{transform:translateY(-1px);box-shadow:0 6px 22px rgba(108,99,255,.5);}
.btn-nav:disabled{opacity:.35;cursor:not-allowed;transform:none!important;}

/* ── RESULT */
#screen-result{display:none;animation:fadeUp .4s ease;}
.result-ring{width:130px;height:130px;border-radius:50%;
  background:conic-gradient(var(--accent) 0%,var(--accent2) var(--pct),var(--border) var(--pct));
  display:flex;align-items:center;justify-content:center;margin:0 auto 18px;position:relative;}
.result-ring::before{content:'';position:absolute;inset:11px;background:var(--surface);border-radius:50%;}
.result-ring .ring-val{position:relative;z-index:1;font-size:24px;font-weight:800;}
.result-hero{text-align:center;padding:36px 20px 24px;}
.result-hero h2{font-size:21px;font-weight:700;margin-bottom:7px;}
.result-hero p{color:var(--muted);font-size:14px;}
.result-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:20px 0;}
.rs-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);
  padding:14px;text-align:center;}
.rs-card .rs-val{font-size:22px;font-weight:800;margin-bottom:3px;}
.rs-card .rs-lbl{font-size:10px;color:var(--muted);}
.rs-card.green .rs-val{color:var(--green);}
.rs-card.red   .rs-val{color:var(--red);}
.rs-card.yellow .rs-val{color:var(--yellow);}
.part-breakdown{}
.pb-item{display:flex;align-items:center;gap:10px;padding:10px 0;border-bottom:1px solid var(--border);}
.pb-item:last-child{border-bottom:none;}
.pb-name{flex:1;font-size:12px;}
.pb-bar{height:5px;background:var(--border);border-radius:3px;overflow:hidden;width:100px;}
.pb-fill{height:100%;border-radius:3px;background:linear-gradient(to right,var(--accent),var(--accent2));}
.pb-score{font-size:12px;font-weight:700;width:44px;text-align:right;}

/* ── REVIEW TABLE */
.review-table{overflow-x:auto;margin-bottom:18px;}
.review-table table{width:100%;border-collapse:collapse;font-size:12px;}
.review-table th{background:var(--surface2);color:var(--muted);padding:8px 10px;text-align:left;
  font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:.5px;}
.review-table td{padding:8px 10px;border-bottom:1px solid var(--border);}
.review-table tr:last-child td{border-bottom:none;}
.tag-correct{color:var(--green);font-weight:700;}
.tag-wrong{color:var(--red);font-weight:700;}
.tag-skip{color:var(--muted);}

/* ── BUTTONS */
.btn-full{width:100%;padding:14px;border-radius:11px;border:none;cursor:pointer;font-size:14px;font-weight:700;
  background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;
  box-shadow:0 4px 18px rgba(108,99,255,.4);transition:all .2s;}
.btn-full:hover{transform:translateY(-2px);box-shadow:0 8px 28px rgba(108,99,255,.5);}
.btn-outline{width:100%;padding:12px;border-radius:11px;border:1px solid var(--border);
  cursor:pointer;font-size:13px;font-weight:600;background:transparent;color:var(--text);
  transition:all .2s;margin-top:8px;}
.btn-outline:hover{border-color:var(--accent);}
.hidden{display:none!important;}
#toast{position:fixed;bottom:28px;left:50%;transform:translateX(-50%);
  background:var(--surface2);border:1px solid var(--border);color:var(--text);padding:10px 22px;
  border-radius:999px;font-size:13px;font-weight:500;box-shadow:var(--shadow);z-index:999;
  opacity:0;pointer-events:none;transition:opacity .3s;white-space:nowrap;}
#toast.show{opacity:1;}
::-webkit-scrollbar{width:5px;}
::-webkit-scrollbar-track{background:var(--surface);}
::-webkit-scrollbar-thumb{background:var(--border);border-radius:3px;}
  </style>
</head>
<body>

<header>
  <div class="logo-icon">🎧</div>
  <div class="logo-text">
    <h1>EPT Listening Practice</h1>
    <p>TDMU – 5 Practice Tests</p>
  </div>
</header>

<!-- HOME -->
<div id="screen-home">
  <div class="container">
    <div class="home-hero">
      <div class="hero-badge">🎓 Ôn thi EPT-TDMU</div>
      <h2>Luyện Nghe Tiếng Anh</h2>
      <p>5 bài Practice Test · Hình ảnh Part 1 · Script hội thoại · Đáp án chi tiết</p>
    </div>
    <div class="stats-row">
      <div class="stat-card"><div class="num">5</div><div class="lbl">Practice Tests</div></div>
      <div class="stat-card"><div class="num">500</div><div class="lbl">Câu hỏi</div></div>
      <div class="stat-card"><div class="num">4</div><div class="lbl">Phần thi</div></div>
    </div>
    <div class="section-title">📚 Chọn bài thi</div>
    <div class="test-grid" id="test-grid"></div>
    <div class="section-title" style="margin-top:28px">📋 Cấu trúc bài thi Listening</div>
    <div class="part-info-box">
      <div>🖼️ <strong style="color:var(--text)">Part 1 – Photos</strong> &nbsp;(Q1–10): Nghe mô tả – chọn câu đúng nhất cho ảnh</div>
      <div>💬 <strong style="color:var(--text)">Part 2 – Question-Response</strong> &nbsp;(Q11–40): Nghe câu hỏi/nói – chọn câu trả lời</div>
      <div>🗣️ <strong style="color:var(--text)">Part 3 – Conversations</strong> &nbsp;(Q41–70): Nghe hội thoại 2 người – trả lời 3 câu/đoạn</div>
      <div>📢 <strong style="color:var(--text)">Part 4 – Talks</strong> &nbsp;(Q71–100): Nghe bài nói độc thoại – trả lời 3–4 câu/đoạn</div>
    </div>
  </div>
</div>

<!-- EXAM -->
<div id="screen-exam">
  <div class="container">
    <div class="exam-toolbar">
      <button class="btn-back" onclick="goHome()">← Trang chủ</button>
      <div class="exam-title" id="exam-title">Practice Test 1</div>
      <div class="score-badge" id="score-live">Đã làm: <span>0</span>/100</div>
    </div>

    <!-- Audio -->
    <div class="audio-panel">
      <div class="audio-label">🎵 Audio đang phát</div>
      <audio id="audio-el" preload="auto"></audio>
      <div class="player-wrap">
        <div class="player-controls">
          <button class="btn-play" id="btn-play" onclick="togglePlay()">▶</button>
          <div class="player-time-wrap">
            <input type="range" class="player-seek" id="seek-bar" value="0" min="0" step="0.1" oninput="seekAudio(this.value)"/>
            <div class="player-time"><span id="time-cur">0:00</span><span id="time-dur">0:00</span></div>
          </div>
        </div>
        <div class="speed-row">
          <span>Tốc độ:</span>
          <button class="speed-btn active" onclick="setSpeed(0.75,this)">0.75×</button>
          <button class="speed-btn" onclick="setSpeed(1,this)">1×</button>
          <button class="speed-btn" onclick="setSpeed(1.25,this)">1.25×</button>
          <button class="speed-btn" onclick="setSpeed(1.5,this)">1.5×</button>
        </div>
      </div>
    </div>

    <!-- Parts -->
    <div class="parts-nav" id="parts-nav">
      <div class="part-tab active" data-part="0" onclick="filterPart(0,this)">Tất cả</div>
      <div class="part-tab" data-part="1" onclick="filterPart(1,this)">🖼️ Part 1 (1–10)</div>
      <div class="part-tab" data-part="2" onclick="filterPart(2,this)">💬 Part 2 (11–40)</div>
      <div class="part-tab" data-part="3" onclick="filterPart(3,this)">🗣️ Part 3 (41–70)</div>
      <div class="part-tab" data-part="4" onclick="filterPart(4,this)">📢 Part 4 (71–100)</div>
    </div>

    <!-- Map -->
    <div class="q-map-wrap">
      <div class="q-map-title">
        <span id="map-range-label">Câu 1–100</span>
        <span id="map-answered-label" style="color:var(--accent2)"></span>
      </div>
      <div class="question-map" id="question-map"></div>
    </div>

    <!-- Question -->
    <div class="question-panel" id="question-panel">
      <div class="q-header">
        <div class="q-number" id="q-num-label">Câu 1 / 100</div>
        <div class="q-part-badge" id="q-part-badge">Part 1</div>
      </div>

      <!-- Photo (Part 1) -->
      <div id="photo-wrap" class="photo-wrap hidden">
        <img id="photo-img" src="" alt="Photo" loading="lazy"/>
        <div class="photo-label" id="photo-label">📷 Nhìn ảnh và chọn câu mô tả đúng nhất</div>
      </div>

      <!-- Group script (Parts 3, 4) -->
      <div id="group-script-box" class="group-script-box hidden">
        <div class="gs-title">🎧 Nội dung bài nghe</div>
        <div class="gs-body" id="gs-body"></div>
      </div>

      <!-- Question text -->
      <div class="q-text" id="q-text-display"></div>

      <!-- Options -->
      <div class="options-list" id="options-list"></div>

      <div class="q-nav">
        <button class="btn-nav" id="btn-prev" onclick="navigate(-1)">← Trước</button>
        <button class="btn-nav" id="btn-next" onclick="navigate(1)">Tiếp →</button>
        <button class="btn-nav primary" onclick="submitExam()">Nộp bài 📊</button>
      </div>
    </div>
  </div>
</div>

<!-- RESULT -->
<div id="screen-result">
  <div class="container">
    <div class="exam-toolbar">
      <button class="btn-back" onclick="goHome()">← Trang chủ</button>
      <div class="exam-title" id="result-title">Kết quả</div>
    </div>
    <div class="result-hero">
      <div class="result-ring" id="result-ring" style="--pct:0%">
        <div class="ring-val" id="result-pct">0%</div>
      </div>
      <h2 id="result-verdict"></h2>
      <p id="result-msg"></p>
    </div>
    <div class="result-stats">
      <div class="rs-card green"><div class="rs-val" id="r-correct">0</div><div class="rs-lbl">✅ Đúng</div></div>
      <div class="rs-card red">  <div class="rs-val" id="r-wrong">0</div>  <div class="rs-lbl">❌ Sai</div></div>
      <div class="rs-card yellow"><div class="rs-val" id="r-skip">0</div>  <div class="rs-lbl">⭕ Bỏ qua</div></div>
    </div>
    <div class="section-title">Kết quả theo phần</div>
    <div class="part-breakdown" id="part-breakdown"></div>
    <div class="section-title">Chi tiết đáp án</div>
    <div class="review-table">
      <table><thead><tr><th>Câu</th><th>Phần</th><th>Bạn chọn</th><th>Đáp án đúng</th><th>Kết quả</th></tr></thead>
      <tbody id="review-body"></tbody></table>
    </div>
    <button class="btn-full" onclick="retakeExam()">🔄 Làm lại bài này</button>
    <button class="btn-outline" onclick="goHome()">🏠 Chọn bài khác</button>
  </div>
</div>

<div id="toast"></div>

<script>
// ═══════════════════════════ DATA ════════════════════════════
const EPT = __DATA_PLACEHOLDER__;

const ANSWERS = EPT.answers;
const SCRIPTS = EPT.scripts;
const PHOTOS  = EPT.photos;   // only Test 1 photos (key: "1".."10")

const PARTS = [
  {id:1, name:"Part 1 – Photos",            start:1,  end:10,  opts:["A","B","C","D"]},
  {id:2, name:"Part 2 – Question-Response", start:11, end:40,  opts:["A","B","C"]},
  {id:3, name:"Part 3 – Conversations",     start:41, end:70,  opts:["A","B","C","D"]},
  {id:4, name:"Part 4 – Talks",             start:71, end:100, opts:["A","B","C","D"]},
];

const AUDIO = {
  1:"Audio/Practice Test 1.mp3",
  2:"Audio/Practice Test 2.mp3",
  3:"Audio/Practice Test 3.mp3",
  4:"Audio/Practice Test 4.mp3",
  5:"Audio/Practice Test 5.mp3",
};

// ═══════════════════════════ STATE ═══════════════════════════
let curTest=null, userAns={}, curQ=1, submitted=false, partFilter=0, audioEl, speed=0.75;

const SK='ept_prog';
const saveP=()=>{const a=JSON.parse(localStorage.getItem(SK)||'{}');a[curTest]={userAns,submitted};localStorage.setItem(SK,JSON.stringify(a));};
const loadP=(t)=>JSON.parse(localStorage.getItem(SK)||'{}')[t]||null;

// ═══════════════════════════ HOME ════════════════════════════
function renderHome(){
  const grid=document.getElementById('test-grid');
  grid.innerHTML='';
  const all=JSON.parse(localStorage.getItem(SK)||'{}');
  for(let t=1;t<=5;t++){
    const prog=all[t];
    let pct=0,status='Chưa làm';
    if(prog){
      const n=Object.keys(prog.userAns).length;
      pct=Math.round(n);
      status=prog.submitted?'✅ Đã nộp bài':`Đang làm: ${n}/100`;
    }
    const c=document.createElement('div');
    c.className='test-card';c.onclick=()=>startTest(t);
    c.innerHTML=`
      <div class="test-num">${t}</div>
      <div class="test-info" style="flex:1">
        <div class="name">Practice Test ${t}</div>
        <div class="meta">
          <span>🎵 Audio MP3</span><span>📝 100 câu</span>
          ${t==1?'<span>🖼️ Có ảnh Part 1</span>':''}
          <span style="color:var(--accent2)">${status}</span>
        </div>
        ${pct>0?`<div class="test-progress"><div class="test-progress-fill" style="width:${pct}%"></div></div>`:''}
      </div>
      <div class="test-arrow">›</div>`;
    grid.appendChild(c);
  }
}

// ═══════════════════════════ START ═══════════════════════════
function startTest(t){
  curTest=t; submitted=false; partFilter=0;
  const prog=loadP(t);
  if(prog){userAns=prog.userAns||{};submitted=prog.submitted||false;}
  else{userAns={};}
  if(submitted){showResult();return;}

  curQ=1;
  for(let q=1;q<=100;q++){if(!userAns[q]){curQ=q;break;}}

  audioEl=document.getElementById('audio-el');
  audioEl.src=AUDIO[t];audioEl.playbackRate=speed;
  audioEl.addEventListener('timeupdate',updateSeek);
  audioEl.addEventListener('loadedmetadata',()=>{
    document.getElementById('time-dur').textContent=fmtT(audioEl.duration);
    document.getElementById('seek-bar').max=audioEl.duration;
  });
  audioEl.addEventListener('ended',()=>document.getElementById('btn-play').textContent='▶');

  document.getElementById('exam-title').textContent=`Practice Test ${t}`;
  document.getElementById('screen-home').style.display='none';
  document.getElementById('screen-result').style.display='none';
  document.getElementById('screen-exam').style.display='block';
  renderMap();renderQ(curQ);updateScoreBadge();
}

// ═══════════════════════════ AUDIO ═══════════════════════════
function togglePlay(){
  if(!audioEl)return;
  if(audioEl.paused){audioEl.play();document.getElementById('btn-play').textContent='⏸';}
  else{audioEl.pause();document.getElementById('btn-play').textContent='▶';}
}
function seekAudio(v){if(audioEl)audioEl.currentTime=parseFloat(v);}
function updateSeek(){
  if(!audioEl)return;
  document.getElementById('seek-bar').value=audioEl.currentTime;
  document.getElementById('time-cur').textContent=fmtT(audioEl.currentTime);
}
function setSpeed(s,btn){
  speed=s;if(audioEl)audioEl.playbackRate=s;
  document.querySelectorAll('.speed-btn').forEach(b=>b.classList.remove('active'));
  btn.classList.add('active');
}
function fmtT(s){const m=Math.floor(s/60);return`${m}:${Math.floor(s%60).toString().padStart(2,'0')}`;}

// ═══════════════════════════ PART ════════════════════════════
function getPart(q){return PARTS.find(p=>q>=p.start&&q<=p.end)||PARTS[0];}
function filterPart(pid,el){
  partFilter=pid;
  document.querySelectorAll('.part-tab').forEach(t=>t.classList.remove('active'));
  el.classList.add('active');
  renderMap();
  const start=pid===0?1:PARTS[pid-1].start;
  if(curQ<start||(pid!==0&&curQ>PARTS[pid-1].end))renderQ(start);
}

// ═══════════════════════════ MAP ═════════════════════════════
function renderMap(){
  const map=document.getElementById('question-map');
  map.innerHTML='';
  const s=partFilter===0?1:PARTS[partFilter-1].start;
  const e=partFilter===0?100:PARTS[partFilter-1].end;
  document.getElementById('map-range-label').textContent=`Câu ${s}–${e}`;
  for(let q=s;q<=e;q++){
    const d=document.createElement('div');
    d.className='q-dot';d.id=`dot-${q}`;d.textContent=q;
    d.onclick=()=>renderQ(q);
    setDotState(d,q);map.appendChild(d);
  }
  const done=Object.keys(userAns).length;
  document.getElementById('map-answered-label').textContent=`${done}/100 đã trả lời`;
}
function setDotState(d,q){
  d.className='q-dot';
  if(q===curQ){d.classList.add('current');return;}
  if(userAns[q]){
    if(submitted){
      d.classList.add(userAns[q]===ANSWERS[curTest][q]?'correct':'wrong');
    }else{d.classList.add('answered');}
  }
}
function refreshDot(q){const d=document.getElementById(`dot-${q}`);if(d)setDotState(d,q);}

// ═══════════════════════════ RENDER QUESTION ═════════════════
function renderQ(qn){
  const prev=curQ;curQ=qn;
  refreshDot(prev);refreshDot(qn);

  const part=getPart(qn);
  document.getElementById('q-num-label').textContent=`Câu ${qn} / 100`;
  document.getElementById('q-part-badge').textContent=part.name;

  const scriptData=(SCRIPTS[String(curTest)]||{})[String(qn)]||{};
  const ua=userAns[qn]||null;
  const ca=ANSWERS[curTest][String(qn)]||'?';

  // ── Photo (Part 1, Test 1 only for now) ──
  const photoWrap=document.getElementById('photo-wrap');
  const photoImg=document.getElementById('photo-img');
  const photoLbl=document.getElementById('photo-label');
  if(part.id===1&&curTest===1&&PHOTOS[String(qn)]){
    photoWrap.classList.remove('hidden');
    photoImg.src=PHOTOS[String(qn)];
    photoLbl.textContent=`📷 Hình ${qn} – Chọn câu mô tả đúng nhất`;
  }else{
    photoWrap.classList.add('hidden');
    photoImg.src='';
  }

  // ── Group script (Parts 3,4) ──
  const gsBox=document.getElementById('group-script-box');
  const gsBody=document.getElementById('gs-body');
  const grpScript=scriptData.group_script||'';
  if(grpScript&&grpScript.length>10){
    gsBox.classList.remove('hidden');
    gsBody.innerHTML=formatScript(grpScript);
  }else{
    gsBox.classList.add('hidden');
  }

  // ── Question text ──
  const qtEl=document.getElementById('q-text-display');
  const qtxt=scriptData.text||'';
  if(qtxt&&part.id!==1){
    qtEl.classList.remove('hidden');
    qtEl.textContent=qtxt;
  }else if(part.id===1){
    qtEl.classList.remove('hidden');
    qtEl.textContent=`Nghe audio và chọn câu mô tả đúng nhất cho hình số ${qn}.`;
  }else if(part.id===2){
    qtEl.classList.remove('hidden');
    qtEl.textContent='Nghe câu hỏi/câu nói và chọn câu trả lời phù hợp nhất.';
  }else{
    qtEl.classList.remove('hidden');
    qtEl.textContent=`Nghe bài và trả lời câu hỏi số ${qn}.`;
  }

  // ── Options ──
  const optList=document.getElementById('options-list');
  optList.innerHTML='';
  const scriptOpts=scriptData.options||{};
  const opts=part.opts;

  opts.forEach(letter=>{
    const optTxt=scriptOpts[letter]||`Đáp án ${letter}`;
    const btn=document.createElement('button');
    btn.className='option-btn';

    if(submitted){
      if(letter===ca) btn.classList.add('correct');
      else if(letter===ua&&ua!==ca) btn.classList.add('wrong');
    }else if(letter===ua){btn.classList.add('selected');}

    btn.disabled=submitted;
    btn.onclick=()=>selectAns(qn,letter);
    btn.innerHTML=`<div class="opt-letter">${letter}</div><div class="opt-text">${optTxt}</div>`;
    optList.appendChild(btn);
  });

  document.getElementById('btn-prev').disabled=(qn===1);
  document.getElementById('btn-next').disabled=(qn===100);
  document.getElementById('question-panel').scrollIntoView({behavior:'smooth',block:'nearest'});
}

function formatScript(txt){
  return txt.split('\n').map(line=>{
    const m=line.match(/^(Man|Woman|Narrator|Host|Speaker\s?\d*):\s*(.*)/i);
    if(m) return`<span class="gs-line-speaker">${m[1]}:</span> <span class="gs-line-content">${m[2]}</span>\n`;
    return`<span class="gs-line-content">${line}</span>\n`;
  }).join('');
}

// ═══════════════════════════ ANSWER ══════════════════════════
function selectAns(qn,letter){
  if(submitted)return;
  userAns[qn]=letter;saveP();
  renderQ(qn);updateScoreBadge();
  setTimeout(()=>{if(qn<100)navigate(1);},380);
}
function navigate(dir){
  const next=curQ+dir;
  if(next<1||next>100)return;
  if(partFilter!==0){const p=PARTS[partFilter-1];if(next<p.start||next>p.end)return;}
  renderQ(next);
}
function updateScoreBadge(){
  const n=Object.keys(userAns).length;
  document.getElementById('score-live').innerHTML=`Đã làm: <span>${n}</span>/100`;
}

// ═══════════════════════════ SUBMIT ══════════════════════════
function submitExam(){
  const done=Object.keys(userAns).length;
  if(done<100&&!confirm(`Còn ${100-done} câu chưa trả lời. Nộp bài?`))return;
  submitted=true;saveP();showResult();
}

// ═══════════════════════════ RESULT ══════════════════════════
function showResult(){
  if(audioEl){audioEl.pause();audioEl.src='';}
  document.getElementById('screen-exam').style.display='none';
  document.getElementById('screen-home').style.display='none';
  document.getElementById('screen-result').style.display='block';

  const ans=ANSWERS[curTest];
  let cor=0,wro=0,skip=0;
  for(let q=1;q<=100;q++){
    const ua=userAns[q],ca=ans[String(q)];
    if(!ua)skip++;else if(ua===ca)cor++;else wro++;
  }
  const pct=Math.round((cor/100)*100);
  document.getElementById('result-title').textContent=`Kết quả – Practice Test ${curTest}`;
  document.getElementById('result-pct').textContent=`${pct}%`;
  document.getElementById('result-ring').style.setProperty('--pct',`${pct}%`);
  document.getElementById('r-correct').textContent=cor;
  document.getElementById('r-wrong').textContent=wro;
  document.getElementById('r-skip').textContent=skip;

  const v=pct>=85?'🏆 Xuất sắc!':pct>=70?'✅ Khá tốt!':pct>=50?'📘 Trung bình':'💪 Cần luyện thêm';
  const msg=pct>=85?'Kỹ năng nghe rất tốt! Tiếp tục phát huy.':pct>=70?'Kết quả tốt, ôn thêm phần còn yếu.':pct>=50?'Hãy nghe lại và xem script bài nghe.':'Nghe audio nhiều lần kết hợp xem script để cải thiện.';
  document.getElementById('result-verdict').textContent=v;
  document.getElementById('result-msg').textContent=msg;

  const pb=document.getElementById('part-breakdown');pb.innerHTML='';
  PARTS.forEach(p=>{
    let pc=0,pt=p.end-p.start+1;
    for(let q=p.start;q<=p.end;q++)if(userAns[q]===ans[String(q)])pc++;
    const pp=Math.round((pc/pt)*100);
    pb.innerHTML+=`<div class="pb-item">
      <div class="pb-name">${p.name}</div>
      <div style="flex:1"><div class="pb-bar"><div class="pb-fill" style="width:${pp}%"></div></div></div>
      <div class="pb-score">${pc}/${pt}</div></div>`;
  });

  const tbody=document.getElementById('review-body');tbody.innerHTML='';
  for(let q=1;q<=100;q++){
    const ua=userAns[q]||'—',ca=ans[String(q)];
    const ok=ua===ca,skip=!userAns[q],p=getPart(q);
    tbody.innerHTML+=`<tr>
      <td>${q}</td><td>Part ${p.id}</td>
      <td><strong class="${skip?'tag-skip':ok?'tag-correct':'tag-wrong'}">${ua}</strong></td>
      <td><strong class="tag-correct">${ca}</strong></td>
      <td>${skip?'<span class="tag-skip">⭕</span>':ok?'<span class="tag-correct">✅</span>':'<span class="tag-wrong">❌</span>'}</td>
    </tr>`;
  }
  window.scrollTo({top:0,behavior:'smooth'});
}

function retakeExam(){
  const t=curTest;
  const all=JSON.parse(localStorage.getItem(SK)||'{}');
  delete all[t];localStorage.setItem(SK,JSON.stringify(all));
  userAns={};submitted=false;startTest(t);
}
function goHome(){
  if(audioEl){audioEl.pause();audioEl.src='';}
  document.getElementById('screen-exam').style.display='none';
  document.getElementById('screen-result').style.display='none';
  document.getElementById('screen-home').style.display='block';
  renderHome();window.scrollTo({top:0,behavior:'smooth'});
}

renderHome();
</script>
</body>
</html>"""

# Insert data payload
HTML_FINAL = HTML.replace('__DATA_PLACEHOLDER__', payload)
OUT_HTML = 'index.html'

with open(OUT_HTML, 'w', encoding='utf-8') as f:
    f.write(HTML_FINAL)

size_kb = os.path.getsize(OUT_HTML)//1024
print(f"\n✅ Written {OUT_HTML} — {size_kb} KB")
print("Features:")
print("  ✅ Part 1 photos (Test 1, Q1-10) embedded as base64")
print("  ✅ Answer options text (A/B/C/D) from Scripts PDF")
print("  ✅ Group scripts for Parts 3 & 4 (hội thoại + talks)")
print("  ✅ All 5 tests with 100 answers each")
