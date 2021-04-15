# 캠핑
i = 0

while True:
    i += 1
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break

    if v % p > l:
        result = (v // p) * l + l
    else:
        result = (v // p) * l + (v % p)
    
    print("Case {0}: {1}".format(i, result))