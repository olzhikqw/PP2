class Account:
    def __init__(self):
        self.s=""
        self.d=""
    def f(self):
        self.s,self.d=map(int,input().split())
    def g(self):
        if self.s>=self.d:
            print(self.s-self.d)
        else:
            print("Insufficient Funds")
a=Account()
a.f()
a.g()