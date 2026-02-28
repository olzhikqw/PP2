import re
a=input()
s=re.findall(r'\w+',a)
print(len(s))