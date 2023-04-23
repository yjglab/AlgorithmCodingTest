import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
cards = [0] + list(map(int, input().rstrip().split()))
table = [0] * (n + 1)
for i in range(1, n + 1):
    table[i] = cards[i]
    for j in range(1, i + 1):
        table[i] = max(table[i], table[j] + table[i - j])
        if i % j == 0:
            table[i] = max(table[i], cards[j] * (i // j))
print(table[n])