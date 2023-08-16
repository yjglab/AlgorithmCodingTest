import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
from collections import deque
from copy import deepcopy
deq, result = deque(), 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            deq.append((i, j))
def bfs():
    q, array = deq.copy(), deepcopy(arr)
    while q:
        r, c = q.popleft()
        for d in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            dr, dc = r + d[0], c + d[1]
            if dr < 0 or dc < 0 or dr >= n or dc >= m:
                continue
            if not array[dr][dc]:
                array[dr][dc] = 2
                q.append((dr, dc))
    res = 0
    for i in range(n):
        for j in range(m):
            if not array[i][j]:
                res += 1
    return res
def set_wall(cnt):
    global result
    if cnt == 3:
        result = max(result, bfs())
        return
    for i in range(n):
        for j in range(m):
            if not arr[i][j]:
                arr[i][j] = 1
                set_wall(cnt + 1)
                arr[i][j] = 0
set_wall(0)
print(result)