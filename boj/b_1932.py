import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    arr[i][0] = arr[i][0] + arr[i - 1][0]
    arr[i][-1] = arr[i][-1] + arr[i - 1][-1]
    for j in range(1, i):
        arr[i][j] = max(arr[i][j], arr[i][j] + max(arr[i - 1][j - 1], arr[i - 1][j]))
print(max(arr[n - 1]))