import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

arr = list(map(int, list(input().rstrip())))
if sum(arr) % 3 != 0:
    print(-1)
elif 0 not in arr:
    print(-1)
else:
    print("".join(map(str, sorted(arr, reverse=True))))