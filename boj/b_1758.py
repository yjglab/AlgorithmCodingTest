import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = sorted([int(input()) for _ in range(n)], reverse=True)
result = 0
for i in range(n):
    v = arr[i] - i
    if v > 0:
        result += arr[i] - i
print(result)