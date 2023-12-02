import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))

l, r = 0, n - 1
result = [arr[0], arr[-1]]
rs = sum(result)
while l < r:
    s = arr[l] + arr[r]
    if abs(s) < abs(rs):
        result = [arr[l], arr[r]]
        rs = s
    if s < 0:
        l += 1
    else:
        r -= 1
print(*result)