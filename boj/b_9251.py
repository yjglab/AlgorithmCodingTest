import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

a, b = [input().rstrip() for _ in range(2)]
d = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            d[i + 1][j + 1] = d[i][j] + 1
        else:
            d[i + 1][j + 1] = max(d[i + 1][j], d[i][j + 1])
print(d[-1][-1])

#   A C A Y K P
# C 0 1 1 1 1 1
# A 1 1 2 2 2 2
# P 0 0 0 0 0 0
# C 0 0 0 0 0 0
# A 0 0 0 0 0 0
# K 0 0 0 0 0 0