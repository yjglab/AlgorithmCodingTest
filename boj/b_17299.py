import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
table = list(map(int, input().split()))
s = []
c_table = [0] * (max(table) + 1)
result = [-1 for _ in range(n)]
for i in table:
    c_table[i] += 1
for i in range(n):
    while s and c_table[table[s[-1]]] < c_table[table[i]]:
        result[s.pop()] = table[i]
    else:
        s.append(i)
print(*result)