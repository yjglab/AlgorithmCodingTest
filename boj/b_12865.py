import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, k = map(int, input().split())
w, v = [0], [0]
for _ in range(n):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)
table = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j >= w[i]:
            table[i][j] = max(table[i - 1][j], v[i] + table[i][j - w[i]])
        else:
            table[i][j] = table[i - 1][j]
print(table[n][k])