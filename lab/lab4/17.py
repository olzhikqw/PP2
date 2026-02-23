from math import sqrt
r = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
dx = x2 - x1
dy = y2 - y1
dr2 = dx*dx + dy*dy
D = x1*y2 - x2*y1
r2 = r*r
discriminant = r2*dr2 - D*D
if discriminant <= 0:
    print("0.0000000000")
else:
    sqrt_disc = sqrt(discriminant)
    t1 = (- (x1*dx + y1*dy) - sqrt_disc) / dr2
    t2 = (- (x1*dx + y1*dy) + sqrt_disc) / dr2
    t_min = max(0, min(t1, t2))
    t_max = min(1, max(t1, t2))
    if t_max < t_min:
        print("0.0000000000")
    else:
        length = sqrt(dr2) * (t_max - t_min)
        print(f"{length:.10f}")