import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
table = [[0] * 11 for _ in range(n + 1)]
table[1] = [0] + [1 for _ in range(9)] + [0]
for i in range(2, n + 1):
    table[i][0] = table[i - 1][1]
    for j in range(1, 10):
        table[i][j] = table[i - 1][j - 1] + table[i - 1][j + 1]
print(sum(table[n]) % 1000000000)