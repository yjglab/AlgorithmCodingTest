import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = [[] for i in range(max(arr) + 1)]
from itertools import combinations
for i in list(combinations(arr, m)):
    if i not in result[i[0]]:
        result[i[0]].append(i)
for i in result:
    if i:
        for j in i:
            print(*j)