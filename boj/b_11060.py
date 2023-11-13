import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dist = [1001] * n
dist[0] = 0
for i in range(n):
    for j in range(i + 1, i + arr[i] + 1):
        if j >= n:
            break
        dist[j] = min(dist[j], dist[i] + 1)
print(-1 if dist[-1] == 1001 else dist[-1])