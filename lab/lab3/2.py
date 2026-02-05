def f(a):
    q=a
    while True:
        if q%2==0:
            q=q/2
        elif q%3==0:
            q=q/3
        elif q%5==0:
            q=q/5
        elif q==1:
            return "Yes"
        else:
            return "No"
n=int(input())
print(f(n))