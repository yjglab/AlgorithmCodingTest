import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
result = 0
for i in range(n - 2, -1, -1):
    if arr[i + 1] <= arr[i]:
        c = arr[i] - arr[i + 1] + 1
        arr[i] -= c
        result += c
print(result)