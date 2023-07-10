import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, m = int(input()), 9999
primes = [1] * (m + 1)

for i in range(2, int(m ** (1 / 2)) + 1):
    if primes[i]:
        j = 2
        while i * j <= m:
            primes[i * j] = 0
            j += 1
def bfs():
    import collections
    q = collections.deque()
    q.append((a, 0))
    visited = [0] * (m + 1)
    visited[int(a)] = 1

    while q:
        v, c = q.popleft()
        if v == b:
            return c
        for i in range(4):
            for j in range(10):
                trans = int(v[:i] + str(j) + v[i + 1:])
                if visited[trans] or not primes[trans] or trans < 1000:
                    continue
                # print(i, j, trans)
                visited[trans] = 1
                q.append((str(trans), c + 1))
    return -1
for _ in range(n):
    a, b = input().split()
    result = bfs()
    print(result if result != -1 else "Impossible")
