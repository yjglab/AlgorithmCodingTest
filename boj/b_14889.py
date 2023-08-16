import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
result = 101
visited = [0] * (n + 1)
def dfs(v, a):
    global result
    if len(a) == n // 2:
        b = []
        for k in range(1, n + 1):
            if not visited[k]:
                b.append(k)
        t1, t2 = 0, 0
        for i in range(n // 2):
            for j in range(n // 2):
                if i != j:
                    t1 += arr[a[i]][a[j]]
                    t2 += arr[b[i]][b[j]]
        result = min(result, abs(t1 - t2))
        return
    for i in range(v + 1, n + 1):
        if not visited[i]:
            visited[i] = 1
            a.append(i)
            dfs(i, a)
            a.pop()
            visited[i] = 0
for i in range(1, (n // 2) + 1):
    visited[i] = 1
    dfs(i, [i])
    visited[i] = 0
print(result)