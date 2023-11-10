import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

from itertools import combinations
from collections import deque

n = int(input())
arr = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    t = list(map(int, input().split()))
    graph[i].extend(t[1:])
def get_combinations(lists):
    results = []
    for i in range(1, n // 2 + 1):
        for comb in combinations(lists, i):
            results.append((comb, tuple(set(lists) - set(comb))))
    return results
def bfs(area):
    s = area[0]
    q = deque([s])
    visited = [0] * (n + 1)
    visited[s] = 1
    vcnt, cost = 1, 0
    while q:
        v = q.popleft()
        cost += arr[v]
        for i in graph[v]:
            if not visited[i] and i in area:
                visited[i] = 1
                vcnt += 1
                q.append(i)
    return cost, vcnt
result = 1e9
for area in get_combinations([i for i in range(1, n + 1)]):
    a_cost, a_vcnt = bfs(area[0])
    b_cost, b_vcnt = bfs(area[1])
    if a_vcnt + b_vcnt == n:
        result = min(result, abs(a_cost - b_cost))

print(-1 if result == 1e9 else result)