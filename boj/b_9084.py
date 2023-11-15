import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    coins = [0] + list(map(int, input().split()))
    m = int(input())
    table = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        table[i][0] = 1
    for i in range(1, n + 1):
        coin = coins[i]
        for j in range(1, m + 1):
            table[i][j] += table[i - 1][j]
            if j - coin >= 0:
                table[i][j] += table[i][j - coin]
    print(table[n][m])