import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline


arr = list(input().split("-"))
r = []
for i in arr:
    k = list(map(lambda x: int(x), i.split("+")))
    r.append(sum(k))
result = r[0]
for i in range(1, len(arr)):
    result -= r[i]
print(result)




