import re

with open('listening.html', 'r', encoding='utf-8') as f:
    content = f.read()

NEW_TRACKING_URL = 'https://script.google.com/macros/s/AKfycbxv0rRHB-ApxCS75MK_lElRobTPWLDXhOXlOcby6235i3zlTTMC-S892jLiWHLcb74v-w/exec'

tracking_code = f'''const TRACKING_URL = '{NEW_TRACKING_URL}';
function trackUser(mssv, action, details) {{
  if(!mssv) return;
  try {{
    const url = `${{TRACKING_URL}}?mssv=${{encodeURIComponent(mssv)}}&action=${{encodeURIComponent(action)}}&details=${{encodeURIComponent(details)}}`;
    fetch(url, {{ method: 'GET', mode: 'no-cors' }}).catch(e => console.log(e));
  }} catch(e) {{}}
}}
'''

if 'const TRACKING_URL' not in content:
    # Inject fresh
    content = content.replace('<script>', '<script>\n' + tracking_code, 1)
else:
    # Always update to the latest URL
    content = re.sub(
        r"const TRACKING_URL = 'https://script\.google\.com/[^']+';",
        f"const TRACKING_URL = '{NEW_TRACKING_URL}';",
        content
    )

login_patch = '''localStorage.setItem('ept_auth', user);
        trackUser(user, 'Đăng nhập', 'Truy cập trang Listening');'''
if "trackUser(user, 'Đăng nhập'" not in content:
    content = content.replace("localStorage.setItem('ept_auth', user);", login_patch)

result_patch = '''$('rverdict').textContent = v; $('rmsg').textContent = msg;

  if (window.currentUser) {
    trackUser(window.currentUser, 'Nộp bài Listening', `Test: ${curT} - Điểm: ${cor}/100`);
  }'''
if "trackUser(window.currentUser, 'Nộp bài Listening'" not in content:
    content = content.replace("$('rverdict').textContent = v; $('rmsg').textContent = msg;", result_patch)

with open('listening.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('listening.html patched successfully')
