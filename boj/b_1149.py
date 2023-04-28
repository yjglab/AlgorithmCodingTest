import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
table = [arr[0]] + [[0] * 3 for _ in range(n - 1)]

for i in range(1, n):
    table[i][0] = arr[i][0] + min(table[i - 1][1], table[i - 1][2])
    table[i][1] = arr[i][1] + min(table[i - 1][0], table[i - 1][2])
    table[i][2] = arr[i][2] + min(table[i - 1][0], table[i - 1][1])
print(min(table[-1]))