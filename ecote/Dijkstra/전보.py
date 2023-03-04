n, m, start = map(int, input().split())
INF = int(1e9)
path = [INF] * (n + 1)

graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

print(graph)
import heapq
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    path[start] = 0
    while q:
        cost, poped = heapq.heappop(q)
        if cost > path[poped]:
            continue
        for i in graph[poped]:
            if path[i[0]] > cost + i[1]:
                path[i[0]] = cost + i[1]
                heapq.heappush(q, (cost + i[1], i[0]))
cnt = 0
cost = 0
dijkstra(start)
print(path)
for i in path:
    if i != INF:
        cnt += 1
        cost = max(cost, i)
print(cnt - 1, cost)