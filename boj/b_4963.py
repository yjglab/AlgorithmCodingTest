import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

from collections import deque
def bfs(i, j, r, c, arr):
    q = deque()
    q.append((i, j))
    arr[i][j] = 0
    while q:
        qr, qc = q.popleft()
        for d in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)):
            nr, nc = qr + d[0], qc + d[1]
            if nr < 0 or nc < 0 or nr >= r or nc >= c:
                continue
            if arr[nr][nc]:
                arr[nr][nc] = 0
                q.append((nr, nc))

while True:
    c, r = map(int, input().split())
    if [r, c] == [0, 0]:
        break
    arr = [list(map(int, input().split())) for _ in range(r)]
    result = 0
    for i in range(r):
        for j in range(c):
            if arr[i][j]:
                result += 1
                bfs(i, j, r, c, arr)
    print(result)