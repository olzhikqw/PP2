import re
s=input().strip()
matches=re.findall(r'\b\d{2}/\d{2}/\d{4}\b', s)
print(len(matches))