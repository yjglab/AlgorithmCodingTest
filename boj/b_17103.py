import sys, math
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input().rstrip())
m = 1000001
table = [1] * (m)

for i in range(3, int(m ** (1/2)) + 1, 2):
    if table[i]:
        for j in range(i * 2, m, i):
            table[j] = 0

for _ in range(n):
    target = int(input().rstrip())
    if target == 4:
        print(1)
        continue
    cnt = 0
    for i in range(3, int(target / 2) + 1, 2):
        if table[i] and table[target - i]:
            cnt += 1
    print(cnt)