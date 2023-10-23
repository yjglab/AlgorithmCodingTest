import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, target = map(int, input().split())
dist = [i for i in range(target + 1)]
graph = [[] for i in range(target + 1)]
roads = []
for _ in range(n):
    a, b, c = map(int, input().split())
    if b <= target:
        if a not in roads:
            roads.append(a)
        graph[a].append((b, c))
from heapq import heappop, heappush

def dijkstra(s):
    hq = []
    heappush(hq, (dist[s], s))
    while hq:
        d, now = heappop(hq)
        if dist[target] > d + (target - now):
            dist[target] = d + (target - now)
        for i in roads:
            cost = d + (i - now)
            if i > now and cost < dist[i]:
                heappush(hq, (cost, i))
                continue
        for i in graph[now]:
            cost = d + i[1]
            if dist[i[0]] > cost:
                dist[i[0]] = cost
                heappush(hq, (cost, i[0]))
    return dist[target]
result = target
for i in range(target + 1):
    if graph[i]:
        result = min(result, dijkstra(i))
print(result)