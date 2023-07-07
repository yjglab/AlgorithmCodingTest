import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

from itertools import chain, combinations
n = int(input())
arr = list(map(int, input().split()))
arr = list(chain.from_iterable(combinations(arr, r) for r in range(1, n + 1)))
table = {}
for v in arr:
    table[sum(v)] = 1
for i in range(1, 100000 * 20 + 1):
    if i not in table:
        print(i)
        break