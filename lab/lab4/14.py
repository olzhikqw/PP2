from datetime import date, timedelta
def parse(s):
    d, t = s.split()
    y, m, day = map(int, d.split('-'))
    sign = 1 if t[3] == '+' else -1
    hh, mm = map(int, t[4:].split(':'))
    dt = date(y, m, day)
    offset_days = sign * (hh * 60 + mm) / 1440
    return dt.toordinal() - offset_days
a = parse(input())
b = parse(input())
print(int(abs(a - b)))