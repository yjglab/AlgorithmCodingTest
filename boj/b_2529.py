import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = list(input().split())
visited = [0] * 10
result = [sys.maxsize, 0]
def dfs(v, cnt, t):
    global result
    if cnt == n:
        result = [min(str(result[0]), "".join(t)), max(str(result[1]), "".join(t))]
        return
    for k in range(10):
        if arr[cnt] == ">":
            if v > k and not visited[k]:
                t.append(str(k))
                visited[k] = 1
                dfs(k, cnt + 1, t)
                t.pop()
                visited[k] = 0
        elif arr[cnt] == "<":
            if v < k and not visited[k]:
                t.append(str(k))
                visited[k] = 1
                dfs(k, cnt + 1, t)
                t.pop()
                visited[k] = 0
for i in range(10):
    visited[i] = 1
    dfs(i, 0, [str(i)])
    visited[i] = 0
print(result[1])
print(result[0])
