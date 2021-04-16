from collections import deque

n, k = map(int, input().split())

q = deque([])

for i in range(1, n + 1):
    q.append(i)

result = []
count = 1
while q:
    if count % k == 0:
        result.append(q.popleft())
    else:
        q.append(q.popleft())
    count += 1
print(str(result).replace("[", "<").replace("]", ">"))