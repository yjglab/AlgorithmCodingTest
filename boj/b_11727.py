import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
table = [0] * 1001
table[1], table[2] = 1, 3
for i in range(3, n + 1):
    table[i] = table[i - 2] * 2 + table[i - 1]
print(table[n] % 10007)