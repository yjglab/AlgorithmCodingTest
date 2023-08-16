import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = sorted([int(input()) for _ in range(n)], reverse=1)
result = []
for i in range(n):
    result.append(arr[i] * (i + 1))
print(max(result))