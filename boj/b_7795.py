import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    result = 0
    for x in a:
        res = -1
        l, r = 0, m - 1
        while l <= r:
            mid = (l + r) // 2
            if b[mid] < x:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        result += res + 1
    print(result)

