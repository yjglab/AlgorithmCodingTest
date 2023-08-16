n, m = map(int, input().split())
money = []
for _ in range(n):
    money.append(int(input()))
d = [10000] * 10001
d[0] = 0
 
for i in range(n):
    for j in range(money[i], m + 1):
        if d[j - money[i]] != 10000:
            d[j] = min(d[j], d[j - money[i]] + 1)
print(d[m]) if d[m] != 10000 else -1