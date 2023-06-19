import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [[0] * m for _ in range(n)]
arr = [list(input().rstrip()) for _ in range(n)]
result = 0
def dfs(r, c, sr, sc, s, cnt):
    global result
    for d in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = r + d[0], c + d[1]
        if cnt >= 4 and [nr, nc] == [sr, sc]:
            result = 1
            return
        if nr < 0 or nc < 0 or nr >= n or nc >= m:
            continue
        if not visited[nr][nc] and arr[nr][nc] == s:
            visited[nr][nc] = 1
            dfs(nr, nc, sr, sc, s, cnt + 1)
            visited[nr][nc] = 0

for i in range(n):
    for j in range(m):
        if result:
            break
        visited[i][j] = 1
        dfs(i, j, i, j, arr[i][j], 1)
        visited[i][j] = 0
print("Yes" if result else "No")