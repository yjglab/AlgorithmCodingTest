import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, m = map(int, input().split())
sets, inds = [], []
for _ in range(m):
    a, b = map(int, input().split())
    sets.append(a), inds.append(b)
s, i = min(sets), min(inds)
print(min(i * n, s * (n // 6) + i * (n % 6), s * ((n // 6) + 1)))
