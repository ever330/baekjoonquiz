# 주유소
import sys

n = int(sys.stdin.readline())
far = list(map(int, sys.stdin.readline().split()))
costs = list(map(int, sys.stdin.readline().split()))
price = 0

m = costs[0]
for i in range(len(far)):
    if costs[i] < m:
        m = costs[i]
    price += m * far[i]

print(price)