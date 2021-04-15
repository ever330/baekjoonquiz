# 신입사원
import sys

t = int(input())

for i in range(t):
    cnt = 1
    n = int(input())
    p = []
    for j in range(n):
        p.append(list(map(int, sys.stdin.readline().split())))
    p.sort()
    Max = p[0][1]

    for k in range(1, n):
        if Max > p[k][1]:
            cnt += 1
            Max = p[k][1]
    print(cnt)