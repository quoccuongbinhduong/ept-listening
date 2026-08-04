html_path = 'd:/EPT/Listening/listening.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = """.obtn.no .olet{background:var(--red);color:#fff;}
.qnav{display:flex;gap:7px;margin-top:12px;}"""

repl = """.obtn.no .olet{background:var(--red);color:#fff;}
#qexpl {
  margin-top: 12px;
  border-radius: 11px;
  overflow: hidden;
  border: 1px solid rgba(108,99,255,.2);
  background: rgba(108,99,255,.05);
  padding: 12px 14px;
}
.qnav{display:flex;gap:7px;margin-top:12px;}"""

if target in content:
    content = content.replace(target, repl)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Patched listening.html CSS")
else:
    print("Target not found or already patched")
