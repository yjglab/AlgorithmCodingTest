import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    ipt = input().split()
    opn = ipt[0]
    if opn == "push":
        stack.append(ipt[1])
    elif opn == "pop":
        print(stack.pop()) if stack else print(-1)
    elif opn == "size":
        print(len(stack))
    elif opn == "empty":
        print(0) if stack else print(1)
    elif opn == "top":
        print(stack[-1]) if stack else print(-1)