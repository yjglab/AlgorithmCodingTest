import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, s, target, u, d = map(int, input().split())
visited = [0] * (n + 1)
result = 0
while True:
    if visited[s]:
        print("use the stairs")
        break
    visited[s] = 1
    if s == target:
        print(result)
        break
    elif s < target:
        if s + u <= n:
            s += u
        elif s - d >= 1:
            s -= d
    elif s > target:
        if s - d >= 1:
            s -= d
        elif s + u <= n:
            s += u
    result += 1
