import sys, math
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, b = map(int, input().split())
result = ""

while n > 0:
    rest = n % b
    if rest >= 10 and b > 10:
        rest = chr(rest + 55)
    result = str(rest) + result
    n //= b
print(result)