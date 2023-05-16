import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

arr = list(map(int, input().split()))
i = 1
while i:
    if arr == [15 if i % 15 == 0 else i % 15, 28 if i % 28 == 0 else i % 28, 19 if i % 19 == 0 else i % 19]:
        print(i)
        break
    i += 1
