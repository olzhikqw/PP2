a=input()
w={"ONE": '1',"TWO": '2', "THR": '3', "FOU": '4', "FIV": '5', "SIX": '6',"SEV": '7', "EIG": '8', "NIN": '9',"ZER":'0'}
def f(a):
    for i, j in w.items():
        a=a.replace(i,j)
    r= str(eval(a))
    for k in w:
        r=r.replace(w[k],k)
    return r
print(f(a))