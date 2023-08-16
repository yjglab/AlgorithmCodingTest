import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, k = map(int, (input().split()))
from collections import deque
q = deque()
q.append((n, 0))
arr = [0] * 200001
result, finded = 0, 0
while q:
    if n == k:
        break
    now, c = q.popleft()
    arr[now] = 1
    d = [now - 1, now + 1, now * 2]
    for v in d:
        if v < 0 or v >= 100001:
            continue
        if v == k:
            result, finded = c + 1, 1
            break
        if not arr[v]:
            arr[v] = 1
            q.append((v, c + 1))
    if finded:
        break
print(result)