class Rectangle:
    def __init__(self):
        self.s=""
        self.d=""
    def f(self):
        self.s,self.d=map(int,input().split())
    def g(self):
        print(self.s*self.d)
a=Rectangle()
a.f()
a.g()