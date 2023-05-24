import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
def dfs(v, s):
    global result
    if s == k:
        result += 1
    if v == n - 1:
        return
    for i in range(v + 1, n):
        s += arr[i]
        dfs(i, s)
        s -= arr[i]
for i in range(n):
    dfs(i, arr[i])
print(result)