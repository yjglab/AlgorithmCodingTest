import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = list(list(map(int, input().rstrip())) for _ in range(n))
from heapq import heappush, heappop
hq = []
heappush(hq, (0, 0, 0))
visited = [[0] * n for _ in range(n)]
dist = ((-1, 0), (1, 0), (0, -1), (0, 1))
result = 50
while hq:
    cnt, r, c = heappop(hq)
    if [r, c] == [n - 1, n - 1]:
        result = cnt
        break
    for d in dist:
        dr, dc = r + d[0], c + d[1]
        if dr < 0 or dc < 0 or dr >= n or dc >= n:
            continue
        if not visited[dr][dc]:
            if arr[dr][dc]:
                heappush(hq, (cnt, dr, dc))
            else:
                heappush(hq, (cnt + 1, dr, dc))
            visited[dr][dc] = 1
print(result)
