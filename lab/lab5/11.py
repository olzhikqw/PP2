import re
a=input()
s=re.findall(r'[A-Z]',a)
print(len(s))