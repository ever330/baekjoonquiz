import sys

n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
stack = []
result = [-1 for _ in range(n)]

stack.append(0)
i = 1
while stack and i < n:
    while stack and s[stack[-1]] < s[i]:
        result[stack[-1]] = s[i]
        stack.pop()
    stack.append(i)
    i += 1
for i in range(n):
    print(result[i], end=" ")