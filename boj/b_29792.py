import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, m, k = map(int, input().split())
result = []
dmg = [int(input()) for _ in range(n)]
boss, v = [], [0]
for _ in range(k):
    a, b = map(int, input().split())
    boss.append(a), v.append(b)

for i in range(n):
    w = [0]
    for hp in boss:
        time, rest = hp // dmg[i], hp % dmg[i]
        time += 1 if rest else 0
        w.append(time)
    table = [[0] * 901 for _ in range(k + 1)]
    for i in range(1, k + 1):
        for j in range(1, 901):
            if j >= w[i]:
                table[i][j] = max(table[i - 1][j], v[i] + table[i - 1][j - w[i]])
            else:
                table[i][j] = table[i - 1][j]
    result.append(table[k][-1])
print(sum(sorted(result, reverse=1)[:m]))