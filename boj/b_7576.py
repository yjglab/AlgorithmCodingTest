import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

m, n = map(int, input().split())
arr = [list(map(int, list(input().split()))) for _ in range(n)]
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
from collections import deque
q1, q2 = deque(), deque()

def bfs(cnt):
    while q1 or q2:
        cnt += 1
        currq = q1 if q1 else q2
        othrq = q1 if q2 else q2
        while currq:
            qr, qc = currq.popleft()
            for i in range(4):
                nr, nc = qr + dr[i], qc + dc[i]
                if nr < 0 or nc < 0 or nr >= n or nc >= m:
                    continue
                if not arr[nr][nc]:
                    arr[nr][nc] = 1
                    othrq.append((nr, nc))
    return cnt
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q1.append((i, j))
result = bfs(-1)
for i in range(n):
    for j in range(m):
        if not arr[i][j]:
            result = -1
            break
print(result)