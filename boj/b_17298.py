import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
table = list(map(int, input().split()))
s = []
result = [-1 for _ in range(n)]
for i in range(len(table)):
    while s and s[-1][0] < table[i]:
        v, idx = s.pop()
        result[idx] = table[i]
    else:
        s.append((table[i], i))
print(" ".join(map(str, result)))
