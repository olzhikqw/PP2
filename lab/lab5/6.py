import re
a=input()
s=re.search(r'\S+@\S+\.\S+', a)
if(s==None):
    print("No email")
else:
    print(s.group())