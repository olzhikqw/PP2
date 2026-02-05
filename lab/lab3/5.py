class Shape:
    def __init__(self):
        self.s=""
    def f(self):
        self.s=int(input())
    def g(self):
        print(self.s**2)
a=Shape()
a.f()
a.g()