from collections import deque

# 정점, 간선, 탐색을 시작할 정점의 번호 지정
n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]

# m개의 간선이 연결하는 정점의 번호
for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1
visit_list = [0] * (n + 1)

def DFS(v):
    visit_list[v] = 1 # 방문한 점 1로 표시
    print(v, end = ' ')
    for i in range(1, n + 1):
        if (visit_list[i] == 0 and graph[v][i] == 1):
            DFS(i)

def BFS(v):
    queue = deque([v]) # 들려야 할 정점 저장
    visit_list[v] = 0 # 방문한 점 0으로 표시
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in range(1, n + 1):
            if (visit_list[i] == 1 and graph[v][i] == 1):
                queue.append(i)
                visit_list[i] = 0

DFS(v)
print()
BFS(v)