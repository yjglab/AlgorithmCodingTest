import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))

counts = {}
for v in arr:
    if v not in counts:
        counts[v] = 1
    else:
        counts[v] += 1
for v in target:
    if v not in counts:
        print(0, end=" ")
    else:
        print(counts[v], end=" ")