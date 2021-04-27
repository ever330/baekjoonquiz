from collections import deque
import sys

# 미로 크기 입력
n, m = map(int, sys.stdin.readline().split())

# 미로 생성
graph = [sys.stdin.readline() for _ in range(n)]
queue = deque([])
# 방문 경로
visited = [[0] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue.append((0, 0))
visited[0][0] = 1

while queue:
    x, y = queue.popleft()
    # 마지막 도착
    if x == n - 1 and y == m - 1:
        print(visited[x][y])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0 and graph[nx][ny] == '1':
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))