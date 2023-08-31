import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

s1, s2 = input().rstrip(), input().rstrip()
d = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
result = 0
for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i - 1] == s2[j - 1]:
            d[i][j] = d[i - 1][j - 1] + 1
            result = max(result, d[i][j])
print(result)