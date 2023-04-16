import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
result, s, a = [], [], 1
for _ in range(n):
    now = int(input())
    if s and s[-1] == now:
        s.pop()
        result.append("-")
    else:
        for i in range(a, now + 1):
            s.append(i)
            result.append("+")
        s.pop()
        result.append("-")
        a = now + 1
if not s:
    for i in result:
        print(i)
else:
    print("NO")