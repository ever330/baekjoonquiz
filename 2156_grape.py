import sys
input = sys.stdin.readline

# 정수 N을 입력받기
n = int(input())
# 모든 포도주량 정보 입력받기
array = [0] * 10001
d = [0] * 10001
for i in range(1, n + 1):
    array[i] = int(input())

d[1] = array[1]
d[2] = array[1] + array[2]

for i in range(3, n + 1):
    d[i] = max(d[i - 3] + array[i - 1] + array[i], d[i - 2] + array[i], d[i - 1])

print(d[n])