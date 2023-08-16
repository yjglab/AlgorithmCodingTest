import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

arr = list(input().rstrip())
for i, v in enumerate(arr):
    a = ord(v) + 13
    if v.islower():
        arr[i] = chr(96 + a % 122 if a > 122 else a)
    elif v.isupper():
        arr[i] = chr(64 + a % 90 if a > 90 else a)

print("".join(arr))
