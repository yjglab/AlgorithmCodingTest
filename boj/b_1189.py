import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

r, c, k = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]

tr, tc = 0, c - 1
dir = ((-1, 0), (1, 0), (0, -1), (0, 1))
visited = [[0] * c for _ in range(r)]
result = 0
def dfs(sr, sc, cnt):
    global result
    visited[sr][sc] = 1
    if cnt > k:
        return
    if [sr, sc] == [tr, tc] and cnt == k:
        result += 1
        return
    for d in dir:
        dr, dc = sr + d[0], sc + d[1]
        if dr < 0 or dc < 0 or dr >= r or dc >= c:
            continue
        if arr[dr][dc] == "T":
            continue
        if not visited[dr][dc]:
            visited[dr][dc] = 1
            dfs(dr, dc, cnt + 1)
            visited[dr][dc] = 0

dfs(r - 1, 0, 1)
print(result)
