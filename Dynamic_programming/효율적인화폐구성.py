n, m = map(int, input().split())
money = []
for _ in range(n):
    money.append(int(input()))
d = [10000] * 10001
d[0] = 0
 
for i in range(money[0], m + 1):
    for k in money:
        if d[i - k] != 10000:
            d[i] = min(d[i], d[i - k] + 1)
print(d[m]) if d[m] != 10000 else -1