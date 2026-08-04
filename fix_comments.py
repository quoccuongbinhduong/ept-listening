import re

with open('listening.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
"""        // fetch('/api/sync', {
            method: 'POST',
            body: JSON.stringify({user: window.currentUser, state: a})
        }).catch(e => console.error(e));""",
"""        /* fetch('/api/sync', {
            method: 'POST',
            body: JSON.stringify({user: window.currentUser, state: a})
        }).catch(e => console.error(e)); */"""
)

with open('listening.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open('reading.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
"""        // fetch('/api/sync', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({
            username: currentUser,
            state: local
          })
        }).catch(e=>e);""",
"""        /* fetch('/api/sync', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({
            username: currentUser,
            state: local
          })
        }).catch(e=>e); */"""
)

with open('reading.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed block comment syntax error")
