import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0] * (m + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        arr[i][j] = arr[i][j] + max(arr[i - 1][j - 1], arr[i - 1][j], arr[i][j - 1])
print(arr[n][m])
