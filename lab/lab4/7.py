class Reverse:
    def __init__(self, name):
        self.name=name
    def rev(self):
        a=''
        for i in range(len(self.name)-1,-1,-1):
            a+=self.name[i]
        return a

n=input()
w=Reverse(n)
print(w.rev())