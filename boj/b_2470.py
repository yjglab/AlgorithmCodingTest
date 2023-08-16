import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
l, r = 0, n - 1
accr = sys.maxsize
result = []
while l != r:
    now = arr[l] + arr[r]
    p = abs(now)
    if p < accr:
        accr = p
        result = [arr[l], arr[r]]
    if now > 0:
        r -= 1
    elif now < 0:
        l += 1
    else:
        break
print(*result)