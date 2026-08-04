import re
import os

# Fix reading.html
with open('reading.html', 'r', encoding='utf-8') as f:
    r_html = f.read()

r_html = r_html.replace("const res = await fetch('/api/login', {", "/* const res = await fetch('/api/login', {")
r_html = r_html.replace("body: JSON.stringify({user: u, pass: p})\n        });", "body: JSON.stringify({user: u, pass: p})\n        }); */")
r_html = r_html.replace("const data = await res.json();\n        if (data.success) {", "const data = {success: true};\n        if (data.success && u) {")
r_html = r_html.replace("fetch('/reading_data.json", "fetch('reading_data.json")
r_html = r_html.replace("fetch('/api/sync'", "// fetch('/api/sync'")

with open('reading.html', 'w', encoding='utf-8') as f:
    f.write(r_html)

# Fix listening.html
with open('listening.html', 'r', encoding='utf-8') as f:
    l_html = f.read()

l_html = l_html.replace("const res = await fetch('/api/login', {", "/* const res = await fetch('/api/login', {")
l_html = l_html.replace("body: JSON.stringify({user, pass})\n      });", "body: JSON.stringify({user, pass})\n      }); */")
l_html = l_html.replace("const data = await res.json();", "const data = {success: true};")
l_html = l_html.replace("const syncRes = await fetch('/api/sync?user=' + user);", "/* const syncRes = await fetch('/api/sync?user=' + user);")
l_html = l_html.replace("const state = await syncRes.json();", "const state = await syncRes.json(); */ const state = {};")
l_html = l_html.replace("const syncRes = await fetch('/api/sync?user=' + savedUser);", "/* const syncRes = await fetch('/api/sync?user=' + savedUser);")
l_html = l_html.replace("const state = await syncRes.json();", "const state = await syncRes.json(); */ const state = {};")
l_html = l_html.replace("fetch('/api/sync'", "// fetch('/api/sync'")

with open('listening.html', 'w', encoding='utf-8') as f:
    f.write(l_html)

print("Fixed HTML files for Github Pages (bypassed API calls)")
