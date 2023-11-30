import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
dir = ((-1, 0), (1, 0), (0, -1), (0, 1))

from collections import deque
q = []
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            q.append((arr[i][j], i, j))
q1, q2 = deque(sorted(q)), deque()
for _ in range(s):
    currq = q1 if q1 else q2
    othrq = q1 if q2 else q2

    while currq:
        v, qr, qc = currq.popleft()
        for d in dir:
            dr, dc = qr + d[0], qc + d[1]
            if dr < 0 or dc < 0 or dr >= n or dc >= n:
                continue
            if arr[dr][dc]:
                continue
            arr[dr][dc] = v
            othrq.append((v, dr, dc))
print(arr[x - 1][y - 1])
