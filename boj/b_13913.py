import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, k = map(int, (input().split()))
from collections import deque
q = deque()
q.append((n, 0, [n]))
arr = [0] * 200001
while q:
    now, cnt, passed = q.popleft()
    if n > k:
        print(n - k)
        for i in range(n, k - 1, -1):
            print(i, end=" ")
        break
    if now == k:
        print(cnt)
        print(*passed)
        break
    for i in [now - 1, now + 1, now * 2]:
        if i < 0 or i > 100000:
            continue
        if not arr[i]:
            arr[i] = 1
            q.append((i, cnt + 1, passed + [i]))