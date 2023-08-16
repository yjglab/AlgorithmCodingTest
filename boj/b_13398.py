import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
table_a = list(map(int, input().split()))
table_b = [_ for _ in table_a]
for i in range(1, n):
    table_a[i] = max(table_a[i], table_a[i] + table_a[i - 1])
    table_b[i] = max(table_a[i - 1], table_b[i] + table_b[i - 1])
a, b = max(table_a), max(table_b)
print(a if a > b else b)