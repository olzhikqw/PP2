def f(a):
    q=True
    for i in a:
        if int(i)%2!=0:
            q=False
    if q:
        return "Valid"
    else:
        return "Not valid"

n=input()
print(f(n))