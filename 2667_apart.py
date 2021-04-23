# 지도 크기 입력
n = int(input())

# 지도에 0 또는 1 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
sol = []

# DFS로 특정한 집을 방문한 뒤에 연결된 모든 집들도 방문
def DFS(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    # 현재 집을 아직 방문하지 않았다면
    if graph[x][y] == 1:
        # 해당 집 방문 처리
        graph[x][y] = 2
        # 상, 하, 좌, 우의 집도 모두 재귀적으로 호출
        DFS(x - 1, y)
        DFS(x, y - 1)
        DFS(x + 1, y)
        DFS(x, y + 1)
        return True
    return False

result = 0
count = 0

for i in range(n):
    for j in range(n):
        if DFS(i, j) == True:
            result += 1
            now = 0
            for k in range(n):
                now += graph[k].count(2)

            now -= count
            sol.append(now)
            count += now
sol.sort()

print(result)
for i in sol:
    print(i)