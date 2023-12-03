import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, h = map(int, input().split())
d, u = [], []
for _ in range(n // 2):
    d.append(int(input()))
    u.append(int(input()))
d = sorted(d)
u = sorted(map(lambda x: h - x, u))
import bisect
result = []
for i in range(1, h + 1):
    a = n // 2 - bisect.bisect_left(d, i)
    b = bisect.bisect_left(u, i)
    result.append(a + b)
print(min(result), result.count(min(result)))