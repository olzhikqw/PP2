import re
a=input()
s=re.findall(r'\d{2,}', a)
print(*s)