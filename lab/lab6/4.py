n=int(input())
a=map(int,input().split())
b=map(int,input().split())
z=[]
for x,y in zip(a,b):
    z.append(x*y)
print(sum(z))