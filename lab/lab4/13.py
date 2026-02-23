import json
data = json.loads(input())
q = int(input())
for _ in range(q):
    s = input()
    cur = data
    i = 0
    ok = True
    while i < len(s):
        if s[i] == '.':
            i += 1
        elif s[i] == '[':
            j = s.find(']', i)
            if j == -1:
                ok = False
                break
            idx = int(s[i+1:j])
            if type(cur) == list and 0 <= idx < len(cur):
                cur = cur[idx]
            else:
                ok = False
                break
            i = j + 1
        else:
            j = i
            while j < len(s) and s[j] not in '.[':
                j += 1
            key = s[i:j]
            if type(cur) == dict and key in cur:
                cur = cur[key]
            else:
                ok = False
                break
            i = j
    if ok:
        print(json.dumps(cur, separators=(',', ':')))
    else:
        print("NOT_FOUND")