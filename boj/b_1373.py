import sys, math
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = input().rstrip()
result = ""
i = 3

while i - len(n) != 3:
    if i - len(n) == 1:
        result = str(int(n[0]) * 2 + int(n[1])) + result
        break
    if i - len(n) == 2:
        result = str(n[0]) + result
        break
    result = str(int(n[-i]) * 4 + int(n[-i + 1]) * 2 + int(n[-i + 2])) + result
    i += 3
print(result)
