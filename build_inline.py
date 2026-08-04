"""Build final index.html: embed core.json (108KB) inline + load photos.json lazily."""
import json, os

with open('core.json', encoding='utf-8') as f:
    core_raw = f.read()

# Escape any </script> that could break HTML parsing
core_raw = core_raw.replace('</', r'<\/')

html = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>EPT Listening Practice – TDMU</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet"/>
  <style>
:root{--bg:#0d0f1a;--surf:#151828;--surf2:#1e2235;--bdr:#2a2f4a;
  --acc:#6c63ff;--acc2:#a78bfa;--grn:#22c55e;--red:#ef4444;--yel:#facc15;
  --txt:#e2e8f0;--mut:#8892a4;--r:14px;}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--txt);min-height:100vh;overflow-x:hidden;}
body::before{content:'';position:fixed;inset:0;z-index:-1;
  background:radial-gradient(ellipse 70% 50% at 20% 20%,rgba(108,99,255,.15),transparent 60%),
             radial-gradient(ellipse 60% 70% at 80% 80%,rgba(167,139,250,.1),transparent 60%);}
@keyframes fadeUp{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes pulse2{0%,100%{opacity:1}50%{opacity:.3}}
header{background:rgba(21,24,40,.92);backdrop-filter:blur(16px);border-bottom:1px solid var(--bdr);
  padding:11px 16px;position:sticky;top:0;z-index:100;display:flex;align-items:center;gap:11px;}
.logo{width:36px;height:36px;background:linear-gradient(135deg,var(--acc),var(--acc2));
  border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:17px;flex-shrink:0;}
.logo-t h1{font-size:14px;font-weight:700;}.logo-t p{font-size:10px;color:var(--mut);}
.wrap{max-width:820px;margin:0 auto;padding:16px 14px 80px;}
/* HOME */
#home{display:block;animation:fadeUp .35s ease;}
.hero{text-align:center;padding:32px 0 22px;}
.badge2{display:inline-block;background:rgba(108,99,255,.2);border:1px solid rgba(108,99,255,.4);
  color:var(--acc2);font-size:11px;font-weight:600;padding:3px 12px;border-radius:999px;margin-bottom:12px;}
.hero h2{font-size:clamp(22px,5vw,32px);font-weight:800;
  background:linear-gradient(135deg,#fff,var(--acc2));-webkit-background-clip:text;
  -webkit-text-fill-color:transparent;background-clip:text;margin-bottom:7px;}
.hero p{color:var(--mut);font-size:13px;}
.stats{display:flex;gap:9px;flex-wrap:wrap;justify-content:center;margin:16px 0;}
.sc{background:var(--surf);border:1px solid var(--bdr);border-radius:var(--r);
  padding:12px 16px;text-align:center;flex:1;min-width:95px;}
.sc .n{font-size:24px;font-weight:800;color:var(--acc2);}.sc .l{font-size:11px;color:var(--mut);margin-top:2px;}
.slbl{font-size:11px;font-weight:600;color:var(--mut);text-transform:uppercase;letter-spacing:1px;margin:20px 0 8px;}
.tgrid{display:grid;gap:9px;}
.tcard{background:var(--surf);border:1px solid var(--bdr);border-radius:var(--r);
  padding:14px 16px;cursor:pointer;display:flex;align-items:center;gap:12px;
  transition:all .2s;position:relative;overflow:hidden;-webkit-tap-highlight-color:transparent;}
.tcard::before{content:'';position:absolute;left:0;top:0;bottom:0;width:3px;
  background:linear-gradient(var(--acc),var(--acc2));border-radius:3px 0 0 3px;}
.tcard:hover,.tcard:active{border-color:var(--acc);transform:translateY(-1px);
  box-shadow:0 6px 22px rgba(108,99,255,.2);}
.tnum{width:44px;height:44px;flex-shrink:0;background:linear-gradient(135deg,var(--acc),var(--acc2));
  border-radius:11px;display:flex;align-items:center;justify-content:center;font-size:16px;font-weight:800;}
.ti{flex:1;}.ti .name{font-weight:600;font-size:14px;margin-bottom:3px;}
.ti .meta{font-size:11px;color:var(--mut);display:flex;gap:7px;flex-wrap:wrap;}
.tprog{height:3px;background:var(--bdr);border-radius:2px;margin-top:7px;overflow:hidden;}
.tprog-f{height:100%;background:linear-gradient(to right,var(--acc),var(--acc2));transition:width .4s;}
.tarr{color:var(--mut);font-size:16px;margin-left:auto;}
.pinfo{background:var(--surf);border:1px solid var(--bdr);border-radius:var(--r);
  padding:13px 15px;font-size:12px;line-height:2.2;color:var(--mut);}
/* EXAM */
#exam{display:none;animation:fadeUp .3s ease;}
.etbar{display:flex;align-items:center;gap:9px;margin-bottom:12px;flex-wrap:wrap;}
.bbk{background:var(--surf2);border:1px solid var(--bdr);color:var(--txt);border-radius:9px;
  padding:7px 11px;cursor:pointer;font-size:12px;font-weight:500;transition:all .2s;}
.bbk:hover{border-color:var(--acc);}
.etitle{font-weight:700;font-size:14px;flex:1;}
.sbadge{background:var(--surf2);border:1px solid var(--bdr);border-radius:9px;
  padding:6px 13px;font-size:11px;font-weight:600;}
.sbadge span{color:var(--acc2);}
/* AUDIO */
.apanel{background:var(--surf);border:1px solid var(--bdr);border-radius:var(--r);padding:15px;margin-bottom:12px;}
.albl{font-size:10px;color:var(--mut);font-weight:600;text-transform:uppercase;letter-spacing:1px;
  margin-bottom:10px;display:flex;align-items:center;gap:7px;}
.albl::before{content:'';width:7px;height:7px;background:var(--grn);border-radius:50%;animation:pulse2 1.4s infinite;}
.pcontrols{display:flex;align-items:center;gap:9px;}
.bplay{width:46px;height:46px;flex-shrink:0;border-radius:50%;
  background:linear-gradient(135deg,var(--acc),var(--acc2));border:none;cursor:pointer;
  color:#fff;font-size:17px;display:flex;align-items:center;justify-content:center;
  box-shadow:0 4px 16px rgba(108,99,255,.5);transition:transform .15s;}
.bplay:hover{transform:scale(1.08);}.bplay:active{transform:scale(.93);}
.ptw{flex:1;}
.seekbar{width:100%;height:5px;-webkit-appearance:none;appearance:none;background:var(--bdr);
  border-radius:3px;cursor:pointer;outline:none;}
.seekbar::-webkit-slider-thumb{-webkit-appearance:none;width:14px;height:14px;
  background:var(--acc2);border-radius:50%;cursor:pointer;}
.ptimes{display:flex;justify-content:space-between;font-size:10px;color:var(--mut);margin-top:4px;}
.sprow{display:flex;gap:5px;flex-wrap:wrap;align-items:center;margin-top:9px;}
.sprow > span{font-size:11px;color:var(--mut);}
.spbtn{background:var(--surf2);border:1px solid var(--bdr);color:var(--txt);border-radius:6px;
  padding:4px 9px;cursor:pointer;font-size:11px;font-weight:600;transition:all .18s;}
.spbtn:hover{border-color:var(--acc);color:var(--acc2);}
.spbtn.on{background:rgba(108,99,255,.22);border-color:var(--acc);color:var(--acc2);}
/* PART TABS */
.ptabs{display:flex;gap:5px;margin-bottom:12px;flex-wrap:wrap;}
.ptab{padding:5px 11px;border-radius:7px;cursor:pointer;font-size:11px;font-weight:600;
  background:var(--surf2);border:1px solid var(--bdr);transition:all .18s;white-space:nowrap;
  -webkit-tap-highlight-color:transparent;}
.ptab:hover,.ptab:active{border-color:var(--acc);}.ptab.on{background:rgba(108,99,255,.25);border-color:var(--acc);color:var(--acc2);}
/* Q MAP */
.qmwrap{background:var(--surf);border:1px solid var(--bdr);border-radius:var(--r);padding:11px;margin-bottom:12px;}
.qmtop{display:flex;justify-content:space-between;font-size:11px;color:var(--mut);margin-bottom:7px;}
.qmtop span:last-child{color:var(--acc2);font-weight:600;}
.qmap{display:grid;grid-template-columns:repeat(auto-fill,minmax(32px,1fr));gap:4px;}
.qdot{height:32px;border-radius:6px;cursor:pointer;font-size:11px;font-weight:700;
  display:flex;align-items:center;justify-content:center;
  background:var(--surf2);border:1px solid var(--bdr);transition:all .12s;color:var(--mut);
  -webkit-tap-highlight-color:transparent;}
.qdot:hover,.qdot:active{border-color:var(--acc);color:var(--txt);}
.qdot.ans{background:rgba(108,99,255,.2);border-color:var(--acc);color:var(--acc2);}
.qdot.ok{background:rgba(34,197,94,.2);border-color:var(--grn);color:var(--grn);}
.qdot.no{background:rgba(239,68,68,.2);border-color:var(--red);color:var(--red);}
.qdot.cur{background:var(--acc);border-color:var(--acc);color:#fff;transform:scale(1.1);}
/* QUESTION */
.qpanel{background:var(--surf);border:1px solid var(--bdr);border-radius:var(--r);padding:16px;margin-bottom:12px;}
.qhdr{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;}
.qnum-l{font-size:12px;color:var(--mut);font-weight:600;}
.qpart-l{font-size:10px;font-weight:600;background:rgba(108,99,255,.2);color:var(--acc2);padding:2px 9px;border-radius:999px;}
.qphoto{border-radius:11px;overflow:hidden;border:1px solid var(--bdr);margin-bottom:12px;}
.qphoto img{width:100%;display:block;}
.qphoto-lbl{font-size:11px;color:var(--mut);text-align:center;padding:5px;background:var(--surf2);}
.gscript{background:rgba(108,99,255,.07);border:1px solid rgba(108,99,255,.28);
  border-radius:11px;padding:12px 14px;margin-bottom:12px;}
.gstitle{font-size:10px;font-weight:600;color:var(--acc2);text-transform:uppercase;letter-spacing:.5px;margin-bottom:8px;}
.gsbody{font-size:12px;line-height:1.9;white-space:pre-wrap;}
.gs-sp{color:var(--acc2);font-weight:700;}
.qtxt{font-size:13px;line-height:1.6;padding:11px;background:var(--surf2);
  border-radius:9px;border-left:3px solid var(--acc);margin-bottom:12px;}
.opts{display:flex;flex-direction:column;gap:7px;}
.obtn{display:flex;align-items:flex-start;gap:11px;padding:11px 13px;
  background:var(--surf2);border:1.5px solid var(--bdr);border-radius:10px;
  cursor:pointer;width:100%;text-align:left;transition:all .16s;font-size:13px;color:var(--txt);
  -webkit-tap-highlight-color:transparent;}
.obtn:hover,.obtn:active{border-color:var(--acc);background:rgba(108,99,255,.09);}
.obtn.sel{border-color:var(--acc);background:rgba(108,99,255,.18);}
.obtn.ok{border-color:var(--grn);background:rgba(34,197,94,.14);color:var(--grn);}
.obtn.no{border-color:var(--red);background:rgba(239,68,68,.14);color:var(--red);}
.obtn:disabled{cursor:default;}
.olet{width:28px;height:28px;flex-shrink:0;border-radius:50%;background:rgba(255,255,255,.08);
  display:flex;align-items:center;justify-content:center;font-weight:700;font-size:12px;margin-top:1px;}
.obtn.sel .olet{background:var(--acc);color:#fff;}
.obtn.ok .olet{background:var(--grn);color:#fff;}
.obtn.no .olet{background:var(--red);color:#fff;}
.qnav{display:flex;gap:7px;margin-top:12px;}
.bnav{flex:1;padding:10px;border-radius:10px;border:1px solid var(--bdr);
  background:var(--surf2);color:var(--txt);cursor:pointer;font-size:12px;font-weight:600;transition:all .18s;}
.bnav:hover{border-color:var(--acc);}
.bnav.pri{background:linear-gradient(135deg,var(--acc),var(--acc2));border:none;color:#fff;
  box-shadow:0 4px 14px rgba(108,99,255,.4);}
.bnav.pri:hover{transform:translateY(-1px);}
.bnav:disabled{opacity:.3;cursor:not-allowed;}
/* RESULT */
#result{display:none;animation:fadeUp .35s ease;}
.rring{width:120px;height:120px;border-radius:50%;display:flex;align-items:center;
  justify-content:center;margin:0 auto 16px;position:relative;}
.rring::before{content:'';position:absolute;inset:10px;background:var(--surf);border-radius:50%;}
.rval{position:relative;z-index:1;font-size:22px;font-weight:800;}
.rhero{text-align:center;padding:30px 16px 20px;}
.rhero h2{font-size:20px;font-weight:700;margin-bottom:6px;}
.rhero p{color:var(--mut);font-size:13px;}
.rstats{display:grid;grid-template-columns:repeat(3,1fr);gap:9px;margin:18px 0;}
.rsc{background:var(--surf);border:1px solid var(--bdr);border-radius:var(--r);padding:12px;text-align:center;}
.rsc .rv{font-size:20px;font-weight:800;margin-bottom:2px;}.rsc .rl{font-size:10px;color:var(--mut);}
.rsc.g .rv{color:var(--grn);}.rsc.r .rv{color:var(--red);}.rsc.y .rv{color:var(--yel);}
.pbd .pbi{display:flex;align-items:center;gap:9px;padding:9px 0;border-bottom:1px solid var(--bdr);}
.pbd .pbi:last-child{border:none;}.pbn{flex:1;font-size:12px;}
.pbbar{height:4px;background:var(--bdr);border-radius:2px;overflow:hidden;width:90px;}
.pbfill{height:100%;border-radius:2px;background:linear-gradient(to right,var(--acc),var(--acc2));}
.pbsc{font-size:12px;font-weight:700;width:40px;text-align:right;}
.rtbl{overflow-x:auto;margin-bottom:16px;}
.rtbl table{width:100%;border-collapse:collapse;font-size:12px;}
.rtbl th{background:var(--surf2);color:var(--mut);padding:7px 9px;text-align:left;
  font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:.5px;}
.rtbl td{padding:7px 9px;border-bottom:1px solid var(--bdr);}
.rtbl tr:last-child td{border:none;}
.tc{color:var(--grn);font-weight:700;}.tw{color:var(--red);font-weight:700;}.ts{color:var(--mut);}
.bfull{width:100%;padding:13px;border-radius:10px;border:none;cursor:pointer;font-size:14px;font-weight:700;
  background:linear-gradient(135deg,var(--acc),var(--acc2));color:#fff;
  box-shadow:0 4px 16px rgba(108,99,255,.4);transition:all .2s;}
.bfull:hover{transform:translateY(-2px);}
.bout{width:100%;padding:11px;border-radius:10px;border:1px solid var(--bdr);
  cursor:pointer;font-size:13px;font-weight:600;background:transparent;color:var(--txt);
  transition:all .2s;margin-top:8px;}
.bout:hover{border-color:var(--acc);}
.hidden{display:none!important;}
::-webkit-scrollbar{width:4px;}::-webkit-scrollbar-track{background:var(--surf);}
::-webkit-scrollbar-thumb{background:var(--bdr);border-radius:2px;}
  </style>
</head>
<body>
<header>
  <div class="logo">🎧</div>
  <div class="logo-t"><h1>EPT Listening Practice</h1><p>TDMU – 5 Practice Tests</p></div>
</header>

<!-- HOME -->
<div id="home">
 <div class="wrap">
  <div class="hero">
    <div class="badge2">🎓 Ôn thi EPT-TDMU</div>
    <h2>Luyện Nghe Tiếng Anh</h2>
    <p>5 bài Practice Test · Ảnh Part 1 · Script hội thoại · Đáp án chi tiết</p>
  </div>
  <div class="stats">
    <div class="sc"><div class="n">5</div><div class="l">Practice Tests</div></div>
    <div class="sc"><div class="n">500</div><div class="l">Câu hỏi</div></div>
    <div class="sc"><div class="n">4</div><div class="l">Phần thi</div></div>
  </div>
  <div class="slbl">📚 Chọn bài thi</div>
  <div class="tgrid" id="tgrid"></div>
  <div class="slbl" style="margin-top:22px">📋 Cấu trúc bài Listening</div>
  <div class="pinfo">
    <div>🖼️ <strong style="color:var(--txt)">Part 1 – Photos</strong> (Q1–10) · Nghe mô tả → chọn câu đúng nhất cho ảnh</div>
    <div>💬 <strong style="color:var(--txt)">Part 2 – Question-Response</strong> (Q11–40) · Nghe câu hỏi → chọn câu trả lời</div>
    <div>🗣️ <strong style="color:var(--txt)">Part 3 – Conversations</strong> (Q41–70) · Nghe hội thoại → trả lời 3 câu/đoạn</div>
    <div>📢 <strong style="color:var(--txt)">Part 4 – Talks</strong> (Q71–100) · Nghe bài nói → trả lời 3–4 câu/đoạn</div>
  </div>
 </div>
</div>

<!-- EXAM -->
<div id="exam">
 <div class="wrap">
  <div class="etbar">
    <button class="bbk" id="bbk">← Trang chủ</button>
    <div class="etitle" id="etitle">Practice Test 1</div>
    <div class="sbadge" id="sbadge">Đã làm: <span id="sdone">0</span>/100</div>
  </div>
  <div class="apanel">
    <div class="albl">🎵 Audio đang phát</div>
    <audio id="aud" preload="auto"></audio>
    <div class="pcontrols">
      <button class="bplay" id="bplay">▶</button>
      <div class="ptw">
        <input type="range" class="seekbar" id="seekbar" value="0" min="0" step="0.1"/>
        <div class="ptimes"><span id="tcur">0:00</span><span id="tdur">0:00</span></div>
      </div>
    </div>
    <div class="sprow">
      <span>Tốc độ:</span>
      <button class="spbtn on" data-spd="0.75">0.75×</button>
      <button class="spbtn" data-spd="1">1×</button>
      <button class="spbtn" data-spd="1.25">1.25×</button>
      <button class="spbtn" data-spd="1.5">1.5×</button>
    </div>
  </div>
  <div class="ptabs" id="ptabs">
    <div class="ptab on" data-pid="0">Tất cả</div>
    <div class="ptab" data-pid="1">🖼️ Part 1</div>
    <div class="ptab" data-pid="2">💬 Part 2</div>
    <div class="ptab" data-pid="3">🗣️ Part 3</div>
    <div class="ptab" data-pid="4">📢 Part 4</div>
  </div>
  <div class="qmwrap">
    <div class="qmtop"><span id="maplbl">Câu 1–100</span><span id="mapdone"></span></div>
    <div class="qmap" id="qmap"></div>
  </div>
  <div class="qpanel" id="qpanel">
    <div class="qhdr">
      <div class="qnum-l" id="qnuml">Câu 1 / 100</div>
      <div class="qpart-l" id="qpartl">Part 1</div>
    </div>
    <div id="qphoto" class="qphoto hidden"><img id="qpimg" src="" alt=""/><div class="qphoto-lbl">📷 Chọn câu mô tả đúng nhất cho hình</div></div>
    <div id="qgs" class="gscript hidden"><div class="gstitle">🎧 Nội dung bài nghe</div><div class="gsbody" id="gsbody"></div></div>
    <div class="qtxt" id="qtxt"></div>
    <div class="opts" id="opts"></div>
    <div class="qnav">
      <button class="bnav" id="bprev">← Trước</button>
      <button class="bnav" id="bnext">Tiếp →</button>
      <button class="bnav pri" id="bsubmit">Nộp bài 📊</button>
    </div>
  </div>
 </div>
</div>

<!-- RESULT -->
<div id="result">
 <div class="wrap">
  <div class="etbar">
    <button class="bbk" id="bbk2">← Trang chủ</button>
    <div class="etitle" id="rtitle">Kết quả</div>
  </div>
  <div class="rhero">
    <div class="rring" id="rring"><div class="rval" id="rpct">0%</div></div>
    <h2 id="rverdict"></h2><p id="rmsg"></p>
  </div>
  <div class="rstats">
    <div class="rsc g"><div class="rv" id="rcor">0</div><div class="rl">✅ Đúng</div></div>
    <div class="rsc r"><div class="rv" id="rwro">0</div><div class="rl">❌ Sai</div></div>
    <div class="rsc y"><div class="rv" id="rskp">0</div><div class="rl">⭕ Bỏ qua</div></div>
  </div>
  <div class="slbl">Kết quả theo phần</div>
  <div class="pbd" id="pbd"></div>
  <div class="slbl">Chi tiết đáp án</div>
  <div class="rtbl"><table><thead><tr><th>Câu</th><th>Phần</th><th>Bạn chọn</th><th>Đáp án đúng</th><th>KQ</th></tr></thead><tbody id="rtbody"></tbody></table></div>
  <button class="bfull" id="bretake">🔄 Làm lại</button>
  <button class="bout" id="bgohome">🏠 Chọn bài khác</button>
 </div>
</div>

<script>
// ═══════════════════ INLINE DATA (core only) ═══════════════════
const CORE = """ + core_raw + """;

const ANSWERS = CORE.answers;   // {"1":{"1":"B","2":"A",...},...}
const SCRIPTS = CORE.scripts;   // {"1":{"1":{text,options,group_script},...},...}

// Photos loaded lazily from photos.json
let PHOTOS = {};
let photosLoaded = false;

function loadPhotos() {
  if (photosLoaded) return Promise.resolve();
  return fetch('photos.json')
    .then(r => r.json())
    .then(d => { PHOTOS = d.photos || {}; photosLoaded = true; })
    .catch(() => { photosLoaded = true; }); // fail silently
}

// ═══════════════════ CONSTANTS ════════════════════════════════
const PARTS = [
  {id:1, name:'Part 1 – Photos',        s:1,  e:10,  opts:['A','B','C','D']},
  {id:2, name:'Part 2 – Q-Response',    s:11, e:40,  opts:['A','B','C']},
  {id:3, name:'Part 3 – Conversations', s:41, e:70,  opts:['A','B','C','D']},
  {id:4, name:'Part 4 – Talks',         s:71, e:100, opts:['A','B','C','D']},
];
const AUDIO_PATH = {
  1:'Audio/Practice Test 1.mp3', 2:'Audio/Practice Test 2.mp3',
  3:'Audio/Practice Test 3.mp3', 4:'Audio/Practice Test 4.mp3', 5:'Audio/Practice Test 5.mp3'
};
const SK = 'ept3';

// ═══════════════════ STATE ════════════════════════════════════
let curT = null, ua = {}, curQ = 1, isDone = false, pf = 0, spd = 0.75;
let aud = null;

// ═══════════════════ UTILS ════════════════════════════════════
const $ = id => document.getElementById(id);
const getPart = q => PARTS.find(p => q >= p.s && q <= p.e) || PARTS[0];
const fmtT = s => `${Math.floor(s/60)}:${Math.floor(s%60).toString().padStart(2,'0')}`;
const saveState = () => {
  try {
    const a = JSON.parse(localStorage.getItem(SK) || '{}');
    a[curT] = {ua, isDone};
    localStorage.setItem(SK, JSON.stringify(a));
  } catch(e) {}
};
const loadState = t => {
  try { return JSON.parse(localStorage.getItem(SK) || '{}')[t] || null; }
  catch(e) { return null; }
};

// ═══════════════════ HOME ═════════════════════════════════════
function renderHome() {
  const g = $('tgrid');
  g.innerHTML = '';
  const all = JSON.parse(localStorage.getItem(SK) || '{}');
  for (let t = 1; t <= 5; t++) {
    const p = all[t];
    let pct = 0, st = 'Chưa làm';
    if (p) {
      const n = Object.keys(p.ua || {}).length;
      pct = n;
      st = p.isDone ? '✅ Đã nộp bài' : `Đang làm: ${n}/100`;
    }
    const c = document.createElement('div');
    c.className = 'tcard';
    c.innerHTML = `
      <div class="tnum">${t}</div>
      <div class="ti">
        <div class="name">Practice Test ${t}</div>
        <div class="meta">
          <span>🎵 MP3 Audio</span>
          <span>📝 100 câu</span>
          ${t===1 ? '<span>🖼️ Ảnh Part 1</span>' : ''}
          <span style="color:var(--acc2)">${st}</span>
        </div>
        ${pct > 0 ? `<div class="tprog"><div class="tprog-f" style="width:${pct}%"></div></div>` : ''}
      </div>
      <div class="tarr">›</div>`;
    c.addEventListener('click', () => startTest(t));
    g.appendChild(c);
  }
}

// ═══════════════════ START TEST ═══════════════════════════════
function startTest(t) {
  curT = t; isDone = false; pf = 0;
  const p = loadState(t);
  if (p) { ua = p.ua || {}; isDone = p.isDone || false; }
  else { ua = {}; }
  if (isDone) { showResult(); return; }

  // Find first unanswered
  curQ = 1;
  for (let q = 1; q <= 100; q++) { if (!ua[q]) { curQ = q; break; } }

  // Setup audio
  aud = $('aud');
  aud.src = AUDIO_PATH[t];
  aud.playbackRate = spd;
  aud.ontimeupdate = () => {
    $('seekbar').value = aud.currentTime;
    $('tcur').textContent = fmtT(aud.currentTime);
  };
  aud.onloadedmetadata = () => {
    $('tdur').textContent = fmtT(aud.duration);
    $('seekbar').max = aud.duration;
  };
  aud.onended = () => $('bplay').textContent = '▶';

  $('etitle').textContent = `Practice Test ${t}`;

  // Switch screens
  $('home').style.display = 'none';
  $('result').style.display = 'none';
  $('exam').style.display = 'block';

  // Reset part tabs
  document.querySelectorAll('.ptab').forEach((tb, i) => tb.classList.toggle('on', i === 0));

  // Load photos lazily (non-blocking)
  if (t === 1) loadPhotos();

  buildMap();
  renderQ(curQ);
  updateBadge();
}

// ═══════════════════ AUDIO ════════════════════════════════════
$('bplay').addEventListener('click', () => {
  if (!aud) return;
  if (aud.paused) { aud.play(); $('bplay').textContent = '⏸'; }
  else { aud.pause(); $('bplay').textContent = '▶'; }
});
$('seekbar').addEventListener('input', e => { if (aud) aud.currentTime = parseFloat(e.target.value); });
document.querySelectorAll('.spbtn').forEach(btn => {
  btn.addEventListener('click', () => {
    spd = parseFloat(btn.dataset.spd);
    if (aud) aud.playbackRate = spd;
    document.querySelectorAll('.spbtn').forEach(b => b.classList.remove('on'));
    btn.classList.add('on');
  });
});

// ═══════════════════ PART FILTER ══════════════════════════════
document.querySelectorAll('.ptab').forEach(tab => {
  tab.addEventListener('click', () => {
    pf = parseInt(tab.dataset.pid);
    document.querySelectorAll('.ptab').forEach(t => t.classList.remove('on'));
    tab.classList.add('on');
    buildMap();
    const s = pf === 0 ? 1 : PARTS[pf-1].s;
    if (curQ < s || (pf !== 0 && curQ > PARTS[pf-1].e)) renderQ(s);
  });
});

// ═══════════════════ Q MAP ════════════════════════════════════
function buildMap() {
  const s = pf === 0 ? 1 : PARTS[pf-1].s;
  const e = pf === 0 ? 100 : PARTS[pf-1].e;
  $('maplbl').textContent = `Câu ${s}–${e}`;
  const m = $('qmap'); m.innerHTML = '';
  for (let q = s; q <= e; q++) {
    const d = document.createElement('div');
    d.className = 'qdot'; d.id = `d${q}`; d.textContent = q;
    d.addEventListener('click', () => renderQ(q));
    setDot(d, q); m.appendChild(d);
  }
  updateBadge();
}
function setDot(d, q) {
  d.className = 'qdot';
  if (q === curQ) { d.classList.add('cur'); return; }
  if (ua[q]) {
    if (isDone) {
      const ca = (ANSWERS[String(curT)] || {})[String(q)];
      d.classList.add(ua[q] === ca ? 'ok' : 'no');
    } else { d.classList.add('ans'); }
  }
}
function refreshDot(q) { const d = $(`d${q}`); if (d) setDot(d, q); }

// ═══════════════════ RENDER QUESTION ══════════════════════════
function renderQ(qn) {
  const prev = curQ; curQ = qn;
  refreshDot(prev); refreshDot(qn);

  const part = getPart(qn);
  $('qnuml').textContent = `Câu ${qn} / 100`;
  $('qpartl').textContent = part.name;

  const sd = ((SCRIPTS[String(curT)] || {})[String(qn)]) || {};
  const testAns = ANSWERS[String(curT)] || {};
  const ca = testAns[String(qn)] || '?';
  const myAns = ua[qn] || null;

  // Photo (Part 1, Test 1 only)
  const photoWrap = $('qphoto');
  const photoImg = $('qpimg');
  if (part.id === 1 && curT === 1 && PHOTOS[String(qn)]) {
    photoWrap.classList.remove('hidden');
    photoImg.src = PHOTOS[String(qn)];
  } else {
    photoWrap.classList.add('hidden');
    photoImg.src = '';
  }

  // Group script (Parts 3 & 4)
  const grp = sd.group_script || '';
  const gsBox = $('qgs');
  const gsBody = $('gsbody');
  if (grp.length > 10) {
    gsBox.classList.remove('hidden');
    gsBody.innerHTML = fmtScript(grp);
  } else {
    gsBox.classList.add('hidden');
  }

  // Question text
  const qtxtEl = $('qtxt');
  if (sd.text && part.id !== 1) {
    qtxtEl.textContent = sd.text;
  } else if (part.id === 1) {
    qtxtEl.textContent = `Nghe audio và chọn câu mô tả đúng nhất cho hình số ${qn}.`;
  } else if (part.id === 2) {
    qtxtEl.textContent = 'Nghe câu hỏi/câu nói và chọn câu trả lời phù hợp nhất.';
  } else {
    qtxtEl.textContent = `Nghe và trả lời câu hỏi số ${qn}.`;
  }

  // Options
  const oc = $('opts'); oc.innerHTML = '';
  const scriptOpts = sd.options || {};
  part.opts.forEach(letter => {
    const txt = scriptOpts[letter] || `Đáp án ${letter}`;
    const btn = document.createElement('button');
    btn.className = 'obtn';
    if (isDone) {
      if (letter === ca) btn.classList.add('ok');
      else if (letter === myAns && myAns !== ca) btn.classList.add('no');
    } else if (letter === myAns) {
      btn.classList.add('sel');
    }
    btn.disabled = isDone;
    btn.addEventListener('click', () => pick(qn, letter));
    btn.innerHTML = `<div class="olet">${letter}</div><div style="flex:1;line-height:1.5">${txt}</div>`;
    oc.appendChild(btn);
  });

  $('bprev').disabled = (qn === 1);
  $('bnext').disabled = (qn === 100);
  $('qpanel').scrollIntoView({behavior:'smooth', block:'nearest'});
}

function fmtScript(txt) {
  return txt.split('\\n').map(l => {
    const m = l.match(/^(Man|Woman|Narrator|Host|Speaker\\s?\\d*):\\s*(.*)/i);
    if (m) return `<span class="gs-sp">${m[1]}:</span> ${m[2]}\\n`;
    return l + '\\n';
  }).join('');
}

// ═══════════════════ PICK ANSWER ══════════════════════════════
function pick(qn, letter) {
  if (isDone) return;
  ua[qn] = letter; saveState();
  renderQ(qn); updateBadge();
  setTimeout(() => { if (qn < 100) nav(1); }, 350);
}
function nav(d) {
  const next = curQ + d;
  if (next < 1 || next > 100) return;
  if (pf !== 0) { const p = PARTS[pf-1]; if (next < p.s || next > p.e) return; }
  renderQ(next);
}
function updateBadge() {
  const n = Object.keys(ua).length;
  $('sdone').textContent = n;
  const md = $('mapdone'); if (md) md.textContent = `${n}/100 đã trả lời`;
}

// ═══════════════════ NAV BUTTONS ══════════════════════════════
$('bprev').addEventListener('click', () => nav(-1));
$('bnext').addEventListener('click', () => nav(1));
$('bsubmit').addEventListener('click', submit);
$('bbk').addEventListener('click', goHome);
$('bbk2').addEventListener('click', goHome);
$('bretake').addEventListener('click', retake);
$('bgohome').addEventListener('click', goHome);

// ═══════════════════ SUBMIT ═══════════════════════════════════
function submit() {
  const n = Object.keys(ua).length;
  if (n < 100 && !confirm(`Còn ${100-n} câu chưa trả lời. Vẫn nộp bài?`)) return;
  isDone = true; saveState(); showResult();
}

// ═══════════════════ RESULT ═══════════════════════════════════
function showResult() {
  if (aud) { aud.pause(); aud.src = ''; }
  $('exam').style.display = 'none';
  $('home').style.display = 'none';
  $('result').style.display = 'block';

  const ans = ANSWERS[String(curT)] || {};
  let cor = 0, wro = 0, skp = 0;
  for (let q = 1; q <= 100; q++) {
    const u = ua[q], c = ans[String(q)];
    if (!u) skp++; else if (u === c) cor++; else wro++;
  }
  const pct = cor;
  $('rtitle').textContent = `Kết quả – Practice Test ${curT}`;
  $('rpct').textContent = `${pct}%`;
  // Draw ring
  const ring = $('rring');
  ring.style.background = `conic-gradient(var(--acc) 0%, var(--acc2) ${pct}%, var(--bdr) ${pct}%)`;
  $('rcor').textContent = cor; $('rwro').textContent = wro; $('rskp').textContent = skp;

  const v = pct>=85?'🏆 Xuất sắc!':pct>=70?'✅ Khá tốt!':pct>=50?'📘 Cần cố gắng':'💪 Cần luyện thêm';
  const msg = pct>=85?'Kỹ năng nghe rất tốt!':pct>=70?'Ôn thêm phần còn yếu.':pct>=50?'Nghe lại và đọc script.':'Nghe nhiều lần + đọc script nhé.';
  $('rverdict').textContent = v; $('rmsg').textContent = msg;

  const pb = $('pbd'); pb.innerHTML = '';
  PARTS.forEach(p => {
    let pc = 0; const pt = p.e - p.s + 1;
    for (let q = p.s; q <= p.e; q++) if (ua[q] === ans[String(q)]) pc++;
    const pp = Math.round(pc/pt*100);
    pb.innerHTML += `<div class="pbi">
      <div class="pbn">${p.name}</div>
      <div style="flex:1"><div class="pbbar"><div class="pbfill" style="width:${pp}%"></div></div></div>
      <div class="pbsc">${pc}/${pt}</div></div>`;
  });

  const tb = $('rtbody'); tb.innerHTML = '';
  for (let q = 1; q <= 100; q++) {
    const u = ua[q] || '—', c = ans[String(q)], ok = u === c, sk = !ua[q];
    const p = getPart(q);
    tb.innerHTML += `<tr>
      <td>${q}</td><td>Part ${p.id}</td>
      <td><strong class="${sk?'ts':ok?'tc':'tw'}">${u}</strong></td>
      <td><strong class="tc">${c}</strong></td>
      <td>${sk?'<span class="ts">⭕</span>':ok?'<span class="tc">✅</span>':'<span class="tw">❌</span>'}</td>
    </tr>`;
  }
  window.scrollTo({top:0, behavior:'smooth'});
}

function retake() {
  try {
    const a = JSON.parse(localStorage.getItem(SK) || '{}');
    delete a[curT]; localStorage.setItem(SK, JSON.stringify(a));
  } catch(e) {}
  ua = {}; isDone = false; startTest(curT);
}
function goHome() {
  if (aud) { aud.pause(); aud.src = ''; }
  $('exam').style.display = 'none';
  $('result').style.display = 'none';
  $('home').style.display = 'block';
  renderHome(); window.scrollTo({top:0, behavior:'smooth'});
}

// ═══════════════════ BOOT ═════════════════════════════════════
renderHome();
</script>
</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

sz = os.path.getsize('index.html')
print(f"index.html: {sz//1024} KB")

# Quick sanity check - ensure renderHome and ANSWERS are in the file
with open('index.html', encoding='utf-8') as f:
    content = f.read()
checks = {
    'ANSWERS defined': '"1":{"1"' in content,
    'renderHome called': 'renderHome()' in content,
    'tcard click': "addEventListener('click'" in content,
    'startTest func': 'function startTest' in content,
}
for k,v in checks.items():
    print(f"  {'OK' if v else 'FAIL'}: {k}")
