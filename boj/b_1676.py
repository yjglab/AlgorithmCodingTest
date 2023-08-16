import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
result = n
while 1:
    if n == 0:
        result = 1
        break
    if n <= 1:
        break
    n -= 1
    result *= n
cnt, result = 0, str(result)
for i in range(len(result) - 1, -1, -1):
    if result[i] == "0":
        cnt += 1
    else:
        break
print(cnt)