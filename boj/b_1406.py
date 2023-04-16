import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

ls, rs = list(input())[:-1], []
n = int(input())
for _ in range(n):
    inp = list(input().split())
    op = inp[0]
    if op == "L":
        ls and rs.append(ls.pop())
    elif op == "D":
        rs and ls.append(rs.pop())
    elif op == "B":
        ls and ls.pop()
    elif op == "P":
        ls.append(inp[1])
print("".join(ls) + "".join(reversed(rs)))