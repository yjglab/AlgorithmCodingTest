import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

from collections import deque
n = int(input())
dq = deque()

for _ in range(n):
    inp = list(input().split())
    op = inp[0]
    if op == "push_front":
        dq.appendleft(inp[1])
    elif op == "push_back":
        dq.append(inp[1])
    elif op == "pop_front":
        print(dq.popleft() if dq else -1)
    elif op == "pop_back":
        print(dq.pop() if dq else -1)
    elif op == "size":
        print(len(dq))
    elif op == "empty":
        print(0 if dq else 1)
    elif op == "front":
        print(dq[0] if dq else -1)
    elif op == "back":
        print(dq[-1] if dq else -1)