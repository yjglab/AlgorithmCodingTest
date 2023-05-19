import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

l, c = map(int, input().split())
arr = sorted(list(input().split()))
def dfs(s):
    if len(s) == l:
        a, b = 0, 0
        for m in s:
            if m in "aeiou":
                a += 1
            else:
                b += 1
        if a >= 1 and b >= 2:
            return print("".join(s))
        return
    for v in arr:
        if v > s[-1]:
            s.append(v)
            dfs(s)
            s.pop()
for i in range(c - l + 1):
    dfs([arr[i]])