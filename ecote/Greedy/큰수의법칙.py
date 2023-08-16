# 개인 풀이 p.92
n, m, k = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
i = 1
result = 0
while i <= m:
    if i % (k + 1) == 0:
        result += lst[1]
        i += 1
        continue
    result += lst[0]
    i += 1
print(result)

# 2트
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

result, cnt = 0, 0
for i in range(m):
    for j in range(k):
        if cnt >= m:
            break
        result += arr[0]
        cnt += 1
    if cnt >= m:
        break
    elif len(arr) != 1:
        result += arr[1]
        cnt += 1
print(result)