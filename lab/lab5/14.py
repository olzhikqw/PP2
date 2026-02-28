import re
a=input()
s=re.compile(r'^\d+$')
if(s.fullmatch(a)):
    print("Match")
else:
    print("No match")