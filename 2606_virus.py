from collections import deque

# 컴퓨터 수 입력
n = int(input())

# 컴퓨터 연결 수 입력
lines = int(input())
matrix = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(lines):
    x, y = map(int, input().split())
    matrix[x][y] = 1
    matrix[y][x] = 1

def BFS(matrix):
    queue = deque([1])
    visited = [1]
    while queue:
        v = queue.popleft()
        for i in range(len(matrix[v])):
            if matrix[v][i] and i not in visited:
                visited.append(i)
                queue.append(i)
    return len(visited) - 1

print(BFS(matrix))