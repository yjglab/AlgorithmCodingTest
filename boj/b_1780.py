# 컴파일러 문제

import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
counts = {-1: 0, 0: 0, 1: 0}
def match(r, c, m):
    cnt = {-1: 0, 0: 0, 1: 0}
    for i in range(r, r + m):
        for j in range(c, c + m):
            cnt[arr[i][j]] += 1
    if m ** 2 in cnt.values():
        counts[arr[r][c]] += 1
        return
    m //= 3
    if m == 0:
        return
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            match(i * m, j * m, m)
match(0, 0, n)
[print(i) for i in counts.values()]
