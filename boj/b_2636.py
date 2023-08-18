import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(n))
result, time = 0, 0
for i in arr:
    result += i.count(1)
import collections

dist = ((-1, 0), (1, 0), (0, -1), (0, 1))
def bfs():
    q = collections.deque()
    q.append((0, 0))
    target = []
    while q:
        qr, qc = q.popleft()
        for d in dist:
            dr, dc = qr + d[0], qc + d[1]
            if dr < 0 or dc < 0 or dr >= n or dc >= m:
                continue
            if visited[dr][dc]:
                continue
            visited[dr][dc] = 1
            if not arr[dr][dc]:
                q.append((dr, dc))
            else:
                target.append((dr, dc))
    for t in target:
        arr[t[0]][t[1]] = 0
    return len(target)

while 1:
    time += 1
    visited = [[0] * m for _ in range(n)]
    cnt = bfs()
    result -= cnt
    if not result:
        print(time), print(cnt)
        break
