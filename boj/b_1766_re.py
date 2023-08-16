import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, m = map(int, input().split())
inline = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    inline[b] += 1
from collections import deque
q = deque()
for i in range(1, n + 1):
    if not inline[i]:
        q.append(i)
result = []
while q:
    now = q.popleft()
    result.append(now)
    for v in graph[now]:
        inline[v] -= 1
        if inline[v] == 0:
            if not q:
                q.append(v)
            elif v < q[0]:
                q.appendleft(v)
            else:
                q.append(v)
print(*result)