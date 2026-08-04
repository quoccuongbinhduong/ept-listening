import sys

with open('listening.html', 'r', encoding='utf-8') as f:
    content = f.read()

tracking_code = '''const TRACKING_URL = 'https://script.google.com/macros/s/AKfycbxvcYtcNayeYGv2YP5ILD_Aeyc1aJfQ_geSsSeuq_7lLI-ywMxTJ-tN2jkybHcw_j3L5A/exec';
function trackUser(mssv, action, details) {
  if(!mssv) return;
  try {
    const url = `${TRACKING_URL}?mssv=${encodeURIComponent(mssv)}&action=${encodeURIComponent(action)}&details=${encodeURIComponent(details)}`;
    fetch(url, { method: 'GET', mode: 'no-cors' }).catch(e => console.log(e));
  } catch(e) {}
}
'''

if 'const TRACKING_URL' not in content:
    content = content.replace('<script>', '<script>\n' + tracking_code, 1)

login_patch = '''localStorage.setItem('ept_auth', user);
        trackUser(user, 'Đăng nhập', 'Truy cập trang Listening');'''
content = content.replace("localStorage.setItem('ept_auth', user);", login_patch)

result_patch = '''$('rverdict').textContent = v; $('rmsg').textContent = msg;

  if (window.currentUser) {
    trackUser(window.currentUser, 'Nộp bài Listening', `Test: ${curT} - Điểm: ${cor}/100`);
  }'''
content = content.replace("$('rverdict').textContent = v; $('rmsg').textContent = msg;", result_patch)

with open('listening.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('listening.html patched successfully')
