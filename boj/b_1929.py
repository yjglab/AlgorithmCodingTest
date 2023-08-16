import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, m = list(map(int, input().rstrip().split()))
table = [_ for _ in range(m + 1)]
table[1] = 0
for i in range(2, m + 1):
    if not table[i]:
        continue
    for j in range(i * 2, m + 1, i):
        table[j] = 0
for v in range(n, m + 1):
    if table[v]:
        print(v)