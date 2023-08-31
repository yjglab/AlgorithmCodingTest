import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
days = [(0, 0)]
d = [0] * (n + 1)
for _ in range(n):
    days.append(tuple(map(int, input().split())))
for i in range(1, n + 1):
    t, p = days[i]
    d[i] = max(d[i], d[i - 1])
    if i + t - 1 <= n:
        d[i + t - 1] = max(d[i + t - 1], p + d[i - 1])
print(d[-1])