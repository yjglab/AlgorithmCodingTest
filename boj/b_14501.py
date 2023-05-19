import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = [0] + [list(map(int, input().split())) for _ in range(n)]
result = 0
def dfs(s, exp):
    global result
    t = s + arr[s][0]
    if t > n + 1:
        result = max(result, exp)
        return
    if t == n + 1:
        result = max(result, exp + arr[s][1])
        return
    for i in range(t, n + 1):
        dfs(i, exp + arr[s][1])
for i in range(1, n + 1):
    dfs(i, 0)
print(result)