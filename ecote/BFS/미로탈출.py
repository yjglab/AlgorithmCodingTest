n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
from collections import deque
q = deque()
x, y = 0, 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    q.append((x, y))
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if arr[nx][ny] == 0:
                continue
            if nx == 0 and ny == 0:
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[a][b] + 1
                q.append((nx, ny))
bfs(0, 0)
print(arr[n - 1][m - 1])