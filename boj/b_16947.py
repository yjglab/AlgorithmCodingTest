import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
cycle = [3000] * (n + 1)
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (n + 1)
finded = 0
def find_cycle(d, cnt):
    global finded
    if finded:
        return
    for i in graph[d[-1]]:
        if i == d[0] and cnt >= 2:
            for j in d:
                cycle[j] = 0
            finded = 1
            return
        if not visited[i]:
            visited[i] = 1
            find_cycle(d + [i], cnt + 1)
            visited[i] = 0

for i in range(1, n + 1):
    visited[i] = 1
    find_cycle([i], 0)
    visited[i] = 0

from collections import deque
q = deque()
for i in range(1, n + 1):
    if cycle[i] == 0:
        q.append((i, 0))
while q:
    now, d = q.popleft()
    for v in graph[now]:
        if cycle[v] == 3000:
            cycle[v] = d + 1
            q.append((v, d + 1))
print(*cycle[1:])
