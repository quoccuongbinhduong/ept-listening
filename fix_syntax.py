import re
import os

with open('listening.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace("const state = await syncRes.json(); */ const state = {}; */ const state = {};", "const state = {};")
text = text.replace("/* const syncRes = await fetch('/api/sync?user=' + user);", "")
text = text.replace("/* const syncRes = await fetch('/api/sync?user=' + savedUser);", "")

with open('listening.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed syntax error in listening.html")
