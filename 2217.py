# 로프
n = int(input())
rope = []
value = []
for i in range(n):
    rope.append(int(input()))
rope.sort(reverse=True)
for j in range(n):
    value.append(rope[j] * (j+1))
print(max(value))