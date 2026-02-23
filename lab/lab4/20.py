g = 0
def outer(commands):
    n = 0
    def inner():
        nonlocal n
        global g
        for scope, value in commands:
            if scope == "global":
                g += value
            elif scope == "nonlocal":
                n += value
            else:
                x = value
        return n
    return inner()
k = int(input())
commands = []
for _ in range(k):
    s, v = input().split()
    commands.append((s, int(v)))
n = outer(commands)
print(g, n)