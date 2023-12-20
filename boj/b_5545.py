import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
c = int(input())
toppings = sorted([int(input()) for _ in range(n)], reverse=1)
import math
s = c / a

for t in toppings:
    ns = (c + t) / (a + b)
    if s < ns:
        s = ns
        c += t
        a += b
print(math.floor(s))