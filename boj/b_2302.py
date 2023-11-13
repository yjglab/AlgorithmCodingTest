import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
m = int(input())

table = [1] * 41
table[2] = 2
for i in range(3, n + 1):
    table[i] = table[i - 2] + table[i - 1]
s, result = 1, 1
cand = []
for _ in range(m):
    v = int(input())
    cand.append(v - s)
    s = v + 1
cand.append(n - s + 1)
result = 1
for c in cand:
    result *= table[c]
print(result if n > 1 else 1)