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