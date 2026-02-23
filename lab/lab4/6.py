def fib(n):
    a=0
    b=1
    q=[]
    for i in range(n):
       q.append(str(a))
       c=a+b
       a=b
       b=c
    return q
n=int(input()) 
print(','.join(fib(n)))