import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
inf = 1e9
dist = [inf] * (n + 1)
dist[x] = 0
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
from heapq import heappush, heappop
def dijkstra(s):
    hq = []
    heappush(hq, (0, s))
    while hq:
        d, now = heappop(hq)
        if dist[now] < d:
            continue
        for i in graph[now]:
            nd = i[1] + d
            if nd < dist[i[0]]:
                dist[i[0]] = nd
                heappush(hq, (nd, i[0]))

dijkstra(x)
result = []
for i in range(1, n + 1):
    if dist[i] == k:
        result.append(i)
if result:
    [print(i) for i in result]
else:
    print(-1)


