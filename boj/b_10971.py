import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
from itertools import permutations
order = list(permutations([_ for _ in range(n)], n))
result = sys.maxsize

for o in order:
    accu = 0
    stop = 0
    for i in range(n - 1):
        if not arr[o[i]][o[i + 1]] or not arr[o[-1]][o[0]]:
            stop = 1
            break
        accu += arr[o[i]][o[i + 1]]
    if stop:
        continue
    accu += arr[o[-1]][o[0]]
    if result > accu:
        result = accu
print(result)

import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n
result = sys.maxsize
def dfs(start, next, exp, cnt):
    global result
    if exp > result:
        return
    if cnt == n - 1 and arr[next][start]:
        result = min(result, exp + arr[next][start])
        return
    for i in range(n):
        if arr[next][i] and not visited[i]:
            visited[i] = 1
            dfs(start, i, exp + arr[next][i], cnt + 1)
            visited[i] = 0

for i in range(n):
    visited[i] = 1
    dfs(i, i, 0, 0)
    visited[i] = 0
print(result)