import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

r, c, k = map(int, input().split())
graph = [[0] * c for _ in range(r)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
result = 0
dir = ((-1, 0), (1, 0), (0, -1), (0, 1))
def bfs(i, j):
    cnt = 1
    from collections import deque
    q = deque()
    q.append((i, j))
    graph[i][j] = 0
    while q:
        qr, qc = q.popleft()
        for [x, y] in dir:
            dr, dc = qr + x, qc + y
            if dr < 0 or dc < 0 or dr >= r or dc >= c:
                continue
            if not graph[dr][dc]:
                continue
            graph[dr][dc] = 0
            cnt += 1
            q.append((dr, dc))
    return cnt

for i in range(r):
    for j in range(c):
        if graph[i][j]:
            result = max(result, bfs(i, j))
print(result)