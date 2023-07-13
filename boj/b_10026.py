import sys
sys.setrecursionlimit(4000)
sys.stdin = open("input.txt", "r")  # 제거
input = sys.stdin.readline

n = int(input())
strings = [input().rstrip() for _ in range(n)]
arr1, arr2 = [], []
for s in strings:
    arr1.append(list(s))
    arr2.append(list(s.replace("R", "G").replace("G", "R")))
dist = ((-1, 0), (1, 0), (0, -1), (0, 1))
visited1 = [[0] * n for _ in range(n)]
visited2 = [[0] * n for _ in range(n)]


def dfs(r, c, v, arr, visited):
    if visited[r][c]:
        return False
    if arr[r][c] == v:
        visited[r][c] = 1
        for d in dist:
            nr, nc = r + d[0], c + d[1]
            if nr < 0 or nc < 0 or nr >= n or nc >= n:
                continue
            dfs(nr, nc, v, arr, visited)
    return True


r1, r2 = 0, 0
for i in range(n):
    for j in range(n):
        r1 += dfs(i, j, arr1[i][j], arr1, visited1)
        r2 += dfs(i, j, arr2[i][j], arr2, visited2)
print(r1, r2)
