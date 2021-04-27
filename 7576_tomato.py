from collections import deque
import sys

# 가로 m, 세로 n 으로 이루어진 토마토 상자 생성
m, n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 익은 토마토를 기준으로 상, 하, 좌, 우 확인
def BFS():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])

# 상자안의 익은 토마토 확인
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

BFS()
clr = False
result = -2

for i in graph:
    for j in i:
        if j == 0:
            clr == True
        result = max(result, j)

if clr == True:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)