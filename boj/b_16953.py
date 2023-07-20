import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

a, b = map(int, input().split())
result = sys.maxsize
def dfs(n, c):
    global result
    if n > b:
        return
    if n == b:
        result = min(result, c)
        return
    dfs(n * 2, c + 1), dfs(int(str(n) + "1"), c + 1)
dfs(a, 1)
print(-1 if result == sys.maxsize else result)
