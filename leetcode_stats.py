import requests

leetcode_user = "chandan_sh"
url = "https://leetcode-stats-api.herokuapp.com/" + leetcode_user

r = requests.get(url)
data = r.json()

readme_file = "README.md"

with open(readme_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

start = "<!-- LEETCODE:START -->"
end = "<!-- LEETCODE:END -->"

# Build new content
new_stats = f"""
**LeetCode Stats**

- 🟢 Easy: {data['easySolved']} / {data['totalEasy']}
- 🟡 Medium: {data['mediumSolved']} / {data['totalMedium']}
- 🔴 Hard: {data['hardSolved']} / {data['totalHard']}
- 💯 Total Solved: {data['totalSolved']}  
"""

# Replace content
inside = False
with open(readme_file, "w", encoding="utf-8") as f:
    for line in lines:
        if start in line:
            f.write(start + "\n")
            f.write(new_stats + "\n")
            inside = True
        elif end in line:
            f.write(end + "\n")
            inside = False
        elif not inside:
            f.write(line)
