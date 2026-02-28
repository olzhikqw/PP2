import re
a=input()
b=input()
s=re.escape(b)
q=re.findall(s,a)
print(len(q))