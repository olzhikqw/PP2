import re
a=input()
if re.match(r'^[A-Za-z].*\d$', a):
    print("Yes")
else:
    print("No")