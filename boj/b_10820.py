import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

while 1:
    result = [0] * 4
    arr = input().rstrip("\n")
    if arr:
        for v in arr:
            if v.islower():
                result[0] += 1
            elif v.isupper():
                result[1] += 1
            elif v.isdigit():
                result[2] += 1
            elif v.isspace():
                result[3] += 1
        print(*result)
    else:
        break