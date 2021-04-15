# 전자레인지
t = int(input())
a = 0
b = 0
c = 0
while t >= 0:
    if t >= 300:
        a += 1
        t -= 300
    elif t >= 60:
        b += 1
        t -= 60
    elif t >= 10:
        c += 1
        t -= 10
    elif t == 0:
        print(a, b, c)
        break
    else:
        print(-1)
        break