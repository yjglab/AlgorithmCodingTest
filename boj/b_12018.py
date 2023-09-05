import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, m = map(int, input().split())
result = []

for _ in range(n):
    p, l = map(int, input().split())
    arr = sorted(list(map(int, input().split())), reverse=1)
    if l > p:
        result.append(1)
    else:
        result.append(arr[l - 1])
result.sort()
s = 0
for i in range(n):
    s += result[i]
    if s > m:
        print(i)
        break
else:
    print(i + 1)