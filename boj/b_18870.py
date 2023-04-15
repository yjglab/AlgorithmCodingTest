import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
table, cnt = {}, -1
for i, v in enumerate(sorted(arr)):
    if v not in table:
        cnt += 1
        table[v] = cnt
for a in arr:
    print(table[a])