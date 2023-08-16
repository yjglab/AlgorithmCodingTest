import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, k = list(map(int, input().split()))
l = [i + 1 for i in range(n)]
idx = 0
cnt = 1
while len(l):
    if cnt <= k - 1:
        idx, cnt = idx + 1, cnt + 1
    else:
        print(l[idx])
        del l[idx]
        cnt = 1
    if idx >= len(l):
        idx = 0