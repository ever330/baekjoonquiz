import sys
input = sys.stdin.readline

# 정수 N을 입력받기
n, k = map(int, input().split())
d = [[0] * (k + 1) for _ in range(n + 1)]
w = [0]
v = [0]

for i in range(n):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)
for i in range(1, n + 1):
    for j in range(k, 0, -1):
        if j - w[i] >= 0:
            d[i][j] = max(d[i - 1][j], v[i] + d[i - 1][j - w[i]])
        else:
            d[i][j] = d[i - 1][j]
print(max(d[n]))