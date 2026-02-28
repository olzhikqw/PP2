import re
a=input()
def d(x):
    return x.group()*2
s=re.sub(r'\d',d,a)
print(s)