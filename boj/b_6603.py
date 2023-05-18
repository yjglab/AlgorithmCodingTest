import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

while 1:
    arr = list(map(int, input().split()))
    if arr == [0]:
        break
    arr.pop(0)
    from itertools import combinations
    [print(*v) for v in list(combinations(arr, 6))]
    print()

import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

def dfs(s, n, arr):
    if len(s) == 6:
        return print(*s)
    for i in arr:
        if not s:
            s.append(i)
            dfs(s, n, arr)
            s.pop()
        elif s[-1] < i:
            s.append(i)
            dfs(s, n, arr)
            s.pop()

while 1:
    arr = list(map(int, input().split()))
    if arr == [0]:
        break
    n, s = arr.pop(0), []
    dfs(s, n, arr), print()