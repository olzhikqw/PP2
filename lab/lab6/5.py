a=input()
v="aeiouAEIOU"
if any(ch in v for ch in a):
    print("Yes")
else:
    print("No")