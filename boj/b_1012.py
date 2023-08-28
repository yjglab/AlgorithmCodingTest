# bfs
import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

t = int(input())
import collections
dist = ((-1, 0), (1, 0), (0, -1), (0, 1))
def bfs(sr, sc):
    q = collections.deque()
    q.append((sr, sc))
    arr[sr][sc] = 0
    while q:
        qr, qc = q.popleft()
        for d in dist:
            dr, dc = qr + d[0], qc + d[1]
            if dr < 0 or dc < 0 or dr >= n or dc >= m:
                continue
            if arr[dr][dc]:
                q.append((dr, dc))
                arr[dr][dc] = 0
for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    result = 0
    for __ in range(k):
        c, r = map(int, input().split())
        arr[r][c] = 1
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                bfs(i, j)
                result += 1
    print(result)

# dfs
import sys
sys.stdin = open("input.txt", "r") # 제거
sys.setrecursionlimit(4000)
input = sys.stdin.readline

t = int(input())
dist = ((-1, 0), (1, 0), (0, -1), (0, 1))
def dfs(sr, sc):
    arr[sr][sc] = 0
    for d in dist:
        dr, dc = sr + d[0], sc + d[1]
        if dr < 0 or dc < 0 or dr >= n or dc >= m:
            continue
        if arr[dr][dc]:
            arr[dr][dc] = 0
            dfs(dr, dc)
for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    for __ in range(k):
        c, r = map(int, input().split())
        arr[r][c] = 1
    result = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                result += 1
                dfs(i, j)
    print(result)