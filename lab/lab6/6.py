a=int(input())
b=map(int,input().split())
if all(x>=0 for x in b):
    print("Yes")
else:
    print("No")