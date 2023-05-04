import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
table = [0] * n
for i in range(n):
    if i == 0:
        table[i] = arr[i]
        continue
    if i == 1:
        table[i] = arr[i - 1] + arr[i]
        continue
    if i == 2:
        table[i] = max(arr[i - 2] + arr[i], arr[i - 1] + arr[i], arr[i - 2] + arr[i - 1])
        continue
    table[i] = max(table[i - 2] + arr[i], table[i - 3] + arr[i - 1] + arr[i], table[i - 1])
print(table[n - 1])