def power(n):
    for i in range(n+1):
        yield 2**i

n=int(input())
for p in power(n):
    print(p, end=' ')