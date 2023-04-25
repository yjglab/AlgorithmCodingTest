import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
table = [[0, 0] for _ in range(n + 1)]
table[1] = [0, 1]
for i in range(2, n + 1):
    table[i] = [sum(table[i - 1]), table[i - 1][0]]
print(sum(table[n]))