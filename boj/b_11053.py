import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
table = [0] * (max(arr) + 1)
for v in arr:
    table[v] = max(table[:v]) + 1
print(max(table))