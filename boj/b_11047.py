import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
result = 0
for i in range(len(arr) - 1, -1, -1):
    if k % arr[i] != k:
        result += k // arr[i]
        k %= arr[i]
print(result)
