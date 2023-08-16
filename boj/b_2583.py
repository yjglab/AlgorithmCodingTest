import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

m, n, k = map(int, input().split())
arr = [[0] * n for _ in range(m)]
for _ in range(k):
    c1, r1, c2, r2 = map(int, input().split())
    for i in range(r1, r2):
        for j in range(c1, c2):
            arr[i][j] = 1
dist = ((-1, 0), (1, 0), (0, -1), (0, 1))
result = [0, []]
import collections
for i in range(m):
    for j in range(n):
        if not arr[i][j]:
            cnt, arr[i][j] = 1, 1
            result[0] += 1
            q = collections.deque()
            q.append((i, j))
            while q:
                r, c = q.popleft()
                for d in dist:
                    dr, dc = r + d[0], c + d[1]
                    if dr < 0 or dc < 0 or dr >= m or dc >= n:
                        continue
                    if not arr[dr][dc]:
                        arr[dr][dc] = 1
                        cnt += 1
                        q.append((dr, dc))
            result[1].append(cnt)
print(result[0])
print(*sorted(result[1]))
