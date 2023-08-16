import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted([int(input()) for _ in range(m)], reverse=1)
max_v = [0, 0]
for i in range(m - 1, -1, -1):
    cnt = i + 1
    if cnt > n:
        cnt = n
    v = cnt * arr[i]
    if v > max_v[1]:
        max_v = [arr[i], v]
print(*max_v)