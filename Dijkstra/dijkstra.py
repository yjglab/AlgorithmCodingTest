graph = [[],
         [(2, 2), (5, 3), (1, 4)],
         [(3, 3), (2, 4)],
         [(3, 2), (5, 6)],
         [(3, 3), (1, 5)],
         [(1, 3), (2, 6)],
         []]

import heapq
q = []
n = 6
INF = int(1e9)
path = [INF] * (n + 1)

def dijkstra(start):
    heapq.heappush(q, (0, start))
    path[start] = 0
    while q:
        cost, poped = heapq.heappop(q)
        if cost > path[poped]:
            continue
        for c, node in graph[poped]:
            if path[node] > cost + c:
                path[node] = cost + c
                heapq.heappush(q, (cost + c, node))
dijkstra(1)
print(path)
