import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
dr, dc = [-2, -1, -2, -1, 1, 2, 2, 1], [-1, -2, 1, 2, -2, -1, 1, 2]

from collections import deque
for _ in range(n):
    siz = int(input())
    r, c = map(int, input().split())
    tr, tc = map(int, input().split())
    arr = [[0] * siz for __ in range(siz)]
    arr[r][c] = 1
    q = deque()
    q.append((r, c, 0))
    finded, result = 0, 0
    while q:
        if [r, c] == [tr, tc] or finded:
            break
        qr, qc, qn = q.popleft()
        for i in range(8):
            nr, nc = qr + dr[i], qc + dc[i]
            if nr < 0 or nc < 0 or nr >= siz or nc >= siz:
                continue
            if [nr, nc] == [tr, tc]:
                result = qn + 1
                finded = 1
                break
            if not arr[nr][nc]:
                arr[nr][nc] = 1
                q.append((nr, nc, qn + 1))
    print(result)