import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = [[n] * n for _ in range(n)]
dist = [0] * n
for i in range(n):
    for j in range(n):
        if i == j:
            arr[i][j] = 0
while 1:
    a, b = map(int, input().split())
    if [a, b] == [-1, -1]:
        break
    arr[a - 1][b - 1], arr[b - 1][a - 1] = 1, 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
for i in range(n):
    dist[i] = max(arr[i])

t = min(dist)
print(t, dist.count(t))
[print(i + 1, end=" ") if dist[i] == t else None for i in range(n)]
