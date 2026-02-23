def q(a,b):
    for _ in range(b):
        for x in a:
            yield x


a=input().split()
b=int(input())
for i in q(a,b):
    print(i, end=' ')