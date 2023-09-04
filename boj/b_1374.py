import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    _, s, e = map(int, input().split())
    arr.append((s, e))

from heapq import heappop, heappush
h = []
for (s, e) in sorted(arr, key=lambda x: x[0]):
    if h and h[0] <= s:
        heappop(h)
    heappush(h, e)
print(len(h))