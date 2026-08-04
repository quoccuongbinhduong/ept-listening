import re

with open('reading.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
"""      async function checkAuth() {
        const stored = localStorage.getItem('ept_auth');
        if (stored) {
          try {
            const user = JSON.parse(stored);
            userToken = user.username;""",
"""      async function checkAuth() {
        const stored = localStorage.getItem('ept_auth');
        if (stored) {
          try {
            userToken = stored;"""
)

with open('reading.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed JSON.parse in reading.html")
