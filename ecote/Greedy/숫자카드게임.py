# 개인풀이  p.96
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
result = float("-inf")
for i in range(n):
    result = max(result, min(arr[i]))
print(result)