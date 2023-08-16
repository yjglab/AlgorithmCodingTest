import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

nv, kv = map(int, input().split())
table = [[1] * 201 for _ in range(201)]
for k in range(2, kv + 1):
    table[k][1] = k
    for n in range(2, nv + 1):
        table[k][n] = (table[k - 1][n] + table[k][n - 1]) % 1000000000
print(table[kv][nv])
# r=k, c=n
#   1  2  3  4  5  6
#1  1  1  1  1  1  1
#2  2  3  4  5  6  7
#3  3  6 10 15 21 28
#4  4 10 20 35 56 84
