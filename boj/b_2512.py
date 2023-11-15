import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
m = int(input())
l, r = 0, arr[-1]
result = arr[-1]
if sum(arr) <= m:
    print(result)
else:
    while l <= r:
        mid = (l + r) // 2
        sums = sum(map(lambda x: x if x <= mid else mid, arr))
        if sums <= m:
            l = mid + 1
            result = mid
        else:
            r = mid - 1
    print(result)

