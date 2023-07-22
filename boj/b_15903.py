import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
import heapq
heapq.heapify(arr)
for _ in range(m):
    a, b = heapq.heappop(arr), heapq.heappop(arr)
    heapq.heappush(arr, a + b), heapq.heappush(arr, a + b)
print(sum(arr))