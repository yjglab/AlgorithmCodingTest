import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
table_a, table_b = [1] * n, [1] * n
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            table_a[i] = max(table_a[i], table_a[j] + 1)
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if arr[i] > arr[j]:
            table_b[i] = max(table_b[i], table_b[j] + 1)
result = 0
for i in range(n):
    result = max(result, table_a[i] + table_b[i] - 1)
print(result)
