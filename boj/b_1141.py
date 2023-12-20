import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = sorted([input().strip() for _ in range(n)], key=len)
result = 0
for i in range(n):
    c = 0
    for j in range(i + 1, n):
        if arr[j].startswith(arr[i]):
            c = 1
            break
    if not c:
        result += 1
print(result)
                

