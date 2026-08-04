import json
import os

deploy_dir = r"D:\EPT\ept-deploy"
core_file = os.path.join(deploy_dir, "core.json")

# Load existing core.json
with open(core_file, 'r', encoding='utf-8') as f:
    core_data = json.load(f)

if "questions" not in core_data:
    core_data["questions"] = {}

# Load questions_1_2.json (contains Test 1 and Test 3 labeled as "2")
with open('questions_1_2.json', 'r', encoding='utf-8') as f:
    q12 = json.load(f)
    core_data["questions"]["1"] = q12.get("1", {})
    if "2" in q12:
        # Actually this is Test 3
        core_data["questions"]["3"] = q12["2"]

# Load questions_2.json
with open('questions_2.json', 'r', encoding='utf-8') as f:
    q2 = json.load(f)
    if "2" in q2:
        core_data["questions"]["2"] = q2["2"]

# Load questions_4.json
with open('questions_4.json', 'r', encoding='utf-8') as f:
    q4 = json.load(f)
    if "4" in q4:
        core_data["questions"]["4"] = q4["4"]

# Load questions_5.json
with open('questions_5.json', 'r', encoding='utf-8') as f:
    q5 = json.load(f)
    if "5" in q5:
        core_data["questions"]["5"] = q5["5"]

# Save back to core.json
with open(core_file, 'w', encoding='utf-8') as f:
    json.dump(core_data, f, ensure_ascii=False, separators=(',', ':'))

print("Merged all questions into core.json successfully.")
