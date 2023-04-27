import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
table = [_ for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, int(i ** (1 / 2) + 1)):
        if table[i] > table[i - j * j] + 1:
            table[i] = table[i - j * j] + 1
print(table[n])