import sys
content = open('listening.html', encoding='utf-8').read()
idx = content.find("const explBox = $('qexpl');")
if idx == -1:
    print("Not found")
    sys.exit(0)
end_idx = content.find("updateProgress();", idx)
print(content[idx:end_idx])
