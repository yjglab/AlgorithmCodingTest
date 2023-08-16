from math import factorial
import sys
sys.stdin = open("input.txt", "r")  # 제거
input = sys.stdin.readline

n = int(input())
d = [0] * (n + 1)
for _ in range(n):
    n, m = map(int, input().split())
    print(factorial(m) // ((factorial(m - n)) * factorial(n)))
