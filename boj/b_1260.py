import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
graph = [sorted(x) for x in graph]

def dfs(v):
    print(v, end=" ")
    visited[v] = 1
    for i in graph[v]:
        if i and not visited[i]:
            dfs(i)

from collections import deque
def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        now = q.popleft()
        print(now, end=" ")
        for i in graph[now]:
            if i and not visited[i]:
                visited[i] = 1
                q.append(i)

visited = [0] * (n + 1)
dfs(start)
print()
visited = [0] * (n + 1)
bfs(start)




