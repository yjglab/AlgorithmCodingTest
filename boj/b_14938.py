import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, m, r = map(int, input().split())
scores = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
from heapq import heappop, heappush
def dijkstra(start):
    visited = [0] * (n + 1)
    dist = [16] * (n + 1)
    dist[start] = 0
    hq = []
    heappush(hq, (0, start))
    while hq:
        d, now = heappop(hq)
        for i in graph[now]:
            cost = i[1] + d
            if cost <= dist[i[0]] and not visited[i[0]]:
                dist[i[0]] = cost
                heappush(hq, (cost, i[0]))
    result = 0
    for i in range(1, n + 1):
        if dist[i] == 0 or dist[i] <= m:
            result += scores[i]
    return result
result = 0
for i in range(1, n + 1):
    result = max(result, dijkstra(i))
print(result)
