n=int(input())
f=True
for i in range(0,n+1,2):
    if not f:
        print(",",end="")
    print(i, end="")
    f=False