import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
d = [0] * (n + 1)
if n <= 2:
    print(n)
else:
    d[1], d[2] = 1, 2
    for i in range(3, n + 1):
        d[i] = (d[i - 2] + d[i - 1]) % 15746
    print(d[-1])
