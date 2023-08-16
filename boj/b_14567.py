import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

import collections
q = collections.deque()
result = [0] * (n + 1)
for i in range(1, n + 1):
    if not indegree[i]:
        q.append((i, 1))
while q:
    now, r = q.popleft()
    result[now] = r
    for i in graph[now]:
        indegree[i] -= 1
        if not indegree[i]:
            q.append((i, r + 1))
print(*result[1:])