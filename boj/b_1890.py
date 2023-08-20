import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
vst = [[0] * n for _ in range(n)]
s = arr[0][0]
vst[s][0], vst[0][s] = 1, 1

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            break
        if vst[i][j]:
            s = arr[i][j]
            if j + s < n:
                vst[i][j + s] += vst[i][j]
            if i + s < n:
                vst[i + s][j] += vst[i][j]
print(vst[-1][-1])
