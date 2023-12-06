import heapq
hq = []
n = 6
graph = [[],
         [(2, 2), (5, 3), (1, 4)],
         [(3, 3), (2, 4)],
         [(3, 2), (5, 6)],
         [(3, 3), (1, 5)],
         [(1, 3), (2, 6)],
         []]
dist = [1e9] * (n + 1)

def dijkstra(s):
    heapq.heappush(hq, (0, s))
    dist[s] = 0
    while hq:
        cost, now = heapq.heappop(hq)
        if cost > dist[now]:
            continue
        for p, v in graph[now]:
            if dist[v] > cost + p:
                dist[v] = cost + p
                heapq.heappush(hq, (cost + p, v))
dijkstra(1)
print(dist)
