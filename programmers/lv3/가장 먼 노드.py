# 인접 리스트
def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for _ in edge:
        a, b = _
        graph[a].append(b)
        graph[b].append(a)
    from collections import deque
    q = deque()
    q.append((1, -1))
    visited = [0] * (n + 1)
    visited[1] = 1
    
    result = [0] * (n + 1)
    while q:
        now, cnt = q.popleft()
        result[now] += cnt + 1
        for i in graph[now]:
            if not visited[i]:
                visited[i] = 1
                q.append((i, cnt + 1))
    return result.count(max(result))
        
# 인접 행렬 (타임오버)
def solution(n, edge):
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in edge:
        a, b = _
        graph[a][b] = 1
        graph[b][a] = 1
    
    from collections import deque
    q = deque()
    q.append((1, -1))
    visited = [0] * (n + 1)
    visited[1] = 1
    
    result = [0] * (n + 1)
    while q:
        now, cnt = q.popleft()
        result[now] += cnt + 1
        for i in range(len(graph[now])):
            if graph[now][i] and not visited[i]:
                visited[i] = 1
                q.append((i, cnt + 1))
    return result.count(max(result))
        