v=int(input())
a =list(map(int, input().split()))
w=[]
for i in a:
    if i not in w:
        print("YES")
        w.append(i)
    else:
        print("NO")