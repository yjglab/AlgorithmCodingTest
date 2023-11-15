import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]
m = sum(arr) // n
l, r = 1, sum(arr) // n
result = max(arr)
while l <= r:
    mid = (l + r) // 2
    sums = sum(map(lambda x: x // mid, arr))
    if sums < n:
        r = mid - 1
    else:
        l = mid + 1
        result = mid
print(result)