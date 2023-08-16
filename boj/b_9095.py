import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
table = [0] * 11
table[1], table[2], table[3] = 1, 2, 4
for i in range(4, 11):
    table[i] = table[i - 3] + table[i - 2] + table[i - 1]
for _ in range(n):
    number = int(input())
    print(table[number])