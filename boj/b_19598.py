import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())

arr = sorted([list(map(int, input().split())) for _ in range(n)])
print(arr)
from heapq import heappop, heappush
h = []
for (s, e) in arr:
    if h and h[0] <= s:
        heappop(h)
    heappush(h, e)
print(len(h))