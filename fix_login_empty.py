import re

with open('listening.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix checkLogin to require username
text = text.replace(
    "const data = {success: true};",
    "if(!user.trim()) { showLoginError('Vui lòng nhập MSSV (Mã số sinh viên)'); return; }\n        const data = {success: true};"
)

with open('listening.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open('reading.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    "if(!user) return;",
    "if(!user.trim()) { document.getElementById('login-err').innerText = 'Vui lòng nhập MSSV'; return; }"
)

with open('reading.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed empty login bypass")
