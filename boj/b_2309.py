import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

arr = sorted([int(input()) for _ in range(9)])
arr_sum, stop = sum(arr), 0
for i in range(8):
    if stop:
        break
    for j in range(i + 1, 9):
        if arr_sum - (arr[i] + arr[j]) == 100:
            [print(arr[k]) if k not in (i, j) else None for k in range(9)]
            stop = 1
            break