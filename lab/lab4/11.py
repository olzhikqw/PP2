import json
def f(a, b):
    for k, v in b.items():
        if v is None:
            a.pop(k, None)
        elif k in a and isinstance(a[k], dict) and isinstance(v, dict):
            f(a[k], v)
        else:
            a[k] = v
    return a
a = json.loads(input())
b = json.loads(input())
print(json.dumps(f(a, b), separators=(',', ':'), sort_keys=True))