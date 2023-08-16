import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = sorted([int(input()) for _ in range(n)], reverse=1)
m = 0
ma = arr[m]
result = -1
for i in range(2, n):
    if ma < arr[i - 1] + arr[i]:
        result = ma + arr[i - 1] + arr[i]
        break
    m += 1
    ma = arr[m]
print(result)