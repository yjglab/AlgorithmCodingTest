import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
from collections import deque
q = deque()
q.append((1, 0, 0))
arr = dict()
arr[(1, 0)] = 0
while q:
    now, clp, cnt = q.popleft()
    if now == n:
        print(arr[(now, clp)])
        break
    if (now, now) not in arr.keys():
        arr[(now, now)] = cnt + 1
        q.append((now, now, cnt + 1))
    if (now + clp, clp) not in arr.keys():
        arr[(now + clp, clp)] = cnt + 1
        q.append((now + clp, clp, cnt + 1))
    if (now - 1, clp) not in arr.keys():
        arr[(now - 1, clp)] = cnt + 1
        q.append((now - 1, clp, cnt + 1))