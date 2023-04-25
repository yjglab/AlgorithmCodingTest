import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
table = [[] for _ in range(max(arr) + 1)]
for v in arr:
    table[v] = max(table[:v], key=lambda x: len(x)) + [v]
result = max(table, key=lambda x: len(x))
print(len(result))
print(*result)