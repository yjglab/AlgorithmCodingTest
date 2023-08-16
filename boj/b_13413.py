import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    result, wc, bc = 0, 0, 0
    a, b = input().rstrip(), input().rstrip()
    for i in range(n):
        if a[i] != b[i]:
            if a[i] == "W":
                wc += 1
            else:
                bc += 1
            result += 1
        if wc > 0 and bc > 0:
            result -= 1
            wc -= 1
            bc -= 1
    print(result)
