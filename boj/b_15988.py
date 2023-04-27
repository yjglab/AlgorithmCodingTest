import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
table = [1, 1, 2] + [0] * 9999998
for i in range(3, 1000001):
    table[i] = (table[i - 1] + table[i - 2] + table[i - 3]) % 1000000009
for i in range(n):
    print(table[int(input())])