import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
dist = ((-1, 0), (1, 0), (0, -1), (0, 1))

import collections
q = collections.deque()
q.append((0, 0))
while q:
    qr, qc = q.popleft()
    for d in dist:
        dr, dc = qr + d[0], qc + d[1]
        if dr < 0 or dc < 0 or dr >= n or dc >= m:
            continue
        if arr[dr][dc] == 1:
            arr[dr][dc] = arr[qr][qc] + 1
            q.append((dr, dc))
print(arr[n - 1][m - 1])
