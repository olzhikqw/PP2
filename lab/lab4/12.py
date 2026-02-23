import json
a = json.loads(input())
b = json.loads(input())
res = []
def f(x, y, path=""):
    if type(x) == dict and type(y) == dict:
        for k in sorted(set(x) | set(y)):
            p = path + "." + k if path else k
            if k not in x:
                res.append((p, "<missing>", json.dumps(y[k], separators=(',', ':'))))
            elif k not in y:
                res.append((p, json.dumps(x[k], separators=(',', ':')), "<missing>"))
            else:
                f(x[k], y[k], p)
    else:
        if x != y:
            res.append((path,
                        json.dumps(x, separators=(',', ':')),
                        json.dumps(y, separators=(',', ':'))))
f(a, b)
if not res:
    print("No differences")
else:
    for p, old, new in sorted(res):
        print(p, ":", old, "->", new)