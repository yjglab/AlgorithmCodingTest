import sys, math
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
table = [0] * (1000001)
table[2], table[3] = 1, 1
for i in range(4, n + 1):
    table[i] = table[i - 1] + 1
    if i % 2 == 0:
        table[i] = min(table[i], table[i // 2] + 1)
    if i % 3 == 0:
        table[i] = min(table[i], table[i // 3] + 1)
print(table[n])