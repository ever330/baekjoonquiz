import sys

n, c = map(int, sys.stdin.readline().split())

array = [int(sys.stdin.readline()) for _ in range(n)]
array.sort()

start, end = 1, max(array) - min(array)
result = 0

while start <= end:
    mid = (start + end) // 2
    first = array[0]
    count = 1

    for i in range(1, len(array)):
        if array[i] >= first + mid:
            count += 1
            first = array[i]
    
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)