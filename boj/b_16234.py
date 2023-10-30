import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0
dir = ((-1, 0), (1, 0), (0, -1), (0, 1))
from collections import deque
def transfer(sr, sc, visited):
    q = deque()
    q.append((sr, sc))
    targets = [(sr, sc)]
    targets_sum = arr[sr][sc]
    while q:
        qr, qc = q.popleft()
        for [x, y] in dir:
            dr, dc = qr + x, qc + y
            if dr < 0 or dc < 0 or dr >= n or dc >= n:
                continue
            if visited[dr][dc]:
                continue
            diff = abs(arr[qr][qc] - arr[dr][dc])
            if diff >= l and diff <= r:
                visited[dr][dc] = 1
                targets.append((dr, dc))
                targets_sum += arr[dr][dc]
                q.append((dr, dc))
    return [targets, targets_sum]
while 1:
    visited = [[0] * n for _ in range(n)]
    candidates = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = 1
                targets, targets_sum = transfer(i, j, visited)
                if len(targets) > 1:
                    candidates.append([targets, targets_sum])
    if not candidates:
        print(result)
        break
    for [targets, target_sum] in candidates:
        size = target_sum // len(targets)
        for [tr, tc] in targets:
            arr[tr][tc] = size
    result += 1
