import re
import json

text = response["completion"]

pattern = r'"story":\s*"([^"]+)".*?"description":\s*"([^"]+)".*?"acceptance[_ ]criteri[a]?":\s*"([^"]+)".*?"expected[_ ]benefits":\s*"([^"]+)"'

matches = re.findall(pattern, text, re.DOTALL)

stories = []
for m in matches:
    stories.append({
        "story": m[0],
        "description": m[1],
        "acceptance_criteria": m[2],
        "expected_benefits": m[3]
    })

print(json.dumps(stories, indent=2))
