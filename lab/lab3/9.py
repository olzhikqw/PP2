class Circle:
    def __init__(self):
        self.s=""
    def f(self):
        self.s=int(input())
    def g(self):
        print(f"{self.s**2*3.14159:.2f}")
a=Circle()
a.f()
a.g()