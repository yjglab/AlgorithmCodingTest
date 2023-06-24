import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline
n = int(input())

def bfs(s, marks):
    from collections import deque
    q = deque()
    q.append((s, True))
    marks[s] = True
    while q:
        now, m = q.popleft()
        for v in graph[now]:
            if marks[v] == m:
                return False
            elif marks[v] == -1:
                marks[v] = not m
                q.append((v, not m))
    return True
for i in range(n):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]

    marks = [-1] * (v + 1)
    for i in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    result = "YES"
    for i in range(1, v + 1):
        if not graph[i]:
            continue
        if marks[i] == -1:
            if not bfs(i, marks):
                result = "NO"
                break
    print(result)

