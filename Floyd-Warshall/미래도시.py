n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n + 1) for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b], graph[b][a] = 1, 1
for i in range(1, n + 1):
    graph[i][i] = 0
x, k = map(int, input().split())
for p in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][p] + graph[p][j])
result = graph[1][k] + graph[k][x]
print(result) if result < INF else -1 