import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, l = map(int, input().split())
arr = sorted(list(map(int, input().split())))

result = 1
s = arr[0]
for i in range(n):
    if arr[i] >= s + l:
        result += 1
        s = arr[i]
print(result)