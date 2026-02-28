import re
a=input()
s=re.findall(r'\b\w{3}\b',a)
print(len(s))