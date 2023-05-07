import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
table = [1] + [0] * n
for i in range(2, n + 1, 2):
    table[i] += table[i - 2] * 3
    for j in range(0, i - 2, 2):
        table[i] += table[j] * 2
print(table[n])