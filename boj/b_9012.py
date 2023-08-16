import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    inp = list(input())
    a, b = 0, 0
    for i in inp:
        if i == "(":
            a += 1
        elif i == ")":
            b += 1
            if a < b:
                break
        if a == b:
            a, b = 0, 0
    print("YES") if a == b else print("NO")