def solution(n, computers):
    visited = [0] * n
    def dfs(v):
        visited[v] = 1
        for i in range(n):
            if i != v and computers[v][i] and not visited[i]:
                dfs(i)
    result = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            result += 1
    return result