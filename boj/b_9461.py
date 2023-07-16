import sys
sys.stdin = open("input.txt", "r")  # 제거
input = sys.stdin.readline

n = int(input())
d = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * 91
for i in range(10, 101):
    d[i] = d[i - 1] + d[i - 5]
for _ in range(n):
    print(d[int(input()) - 1])
