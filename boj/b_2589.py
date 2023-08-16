import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [input().rstrip() for _ in range(n)]
dist = ((-1, 0), (1, 0), (0, -1), (0, 1))
import collections
def bfs(sr, sc):
    q = collections.deque()
    q.append((sr, sc, 0))
    times = [[0] * m for _ in range(n)]
    times[sr][sc] = 1
    t = 0
    while q:
        qr, qc, cnt = q.popleft()
        t = cnt + 1
        for d in dist:
            dr, dc = qr + d[0], qc + d[1]
            if dr < 0 or dc < 0 or dr >= n or dc >= m:
                continue
            if arr[dr][dc] == "L" and times[dr][dc] == 0:
                times[dr][dc] = cnt + 1
                q.append((dr, dc, cnt + 1))
    return t - 1
result = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == "L":
            result = max(result, bfs(i, j))
print(result)
