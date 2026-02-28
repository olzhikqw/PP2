import re
a=input()
s=re.findall(r"\d", a)
print(*s)