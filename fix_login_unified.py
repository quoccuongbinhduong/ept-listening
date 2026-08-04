import re

# Fix listening.html
with open('listening.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace("sessionStorage.setItem('ept_auth'", "localStorage.setItem('ept_auth'")
text = text.replace("sessionStorage.getItem('ept_auth'", "localStorage.getItem('ept_auth'")

with open('listening.html', 'w', encoding='utf-8') as f:
    f.write(text)

# Fix reading.html
with open('reading.html', 'r', encoding='utf-8') as f:
    text = f.read()

# reading.html uses: localStorage.getItem('ept_user') and expects JSON {username: u}
# we will change it to use localStorage.getItem('ept_auth') as a raw string
text = text.replace("const stored = localStorage.getItem('ept_user');", "const stored = localStorage.getItem('ept_auth');")
text = text.replace("if (stored) {\n        const parsed = JSON.parse(stored);\n        userToken = parsed.username;", "if (stored) {\n        userToken = stored;")
text = text.replace("localStorage.setItem('ept_user', JSON.stringify({username: u}));", "localStorage.setItem('ept_auth', u);")

with open('reading.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Unified login across listening and reading")
