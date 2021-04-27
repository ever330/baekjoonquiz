import sys
sys.setrecursionlimit(10000)

# DFS로 특정한 배추를 확인 후 연결된 배추들도 확인
def DFS(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < m):
            if graph[nx][ny] == 1:
                graph[nx][ny] = -1
                DFS(nx, ny)

# 테스트 케이스 T 입력
t = int(sys.stdin.readline())

# 가로 m, 세로 n, 배추의 개수 k 입력
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0] * m for _ in range(n)]

    count = 0

    for _ in range(k):
        X, Y = map(int, sys.stdin.readline().split())
        graph[Y][X] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                DFS(i, j)
                count += 1
    print(count)