import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: (x[1], x[0]))
now, result = arr[0], 1
for i in range(1, n):
    if arr[i][0] >= now[1]:
        now, result = arr[i], result + 1
print(result)