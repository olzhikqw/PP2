import re
a=input()
s=re.compile(r'\w+')
q=re.findall(s,a)
print(len(q))