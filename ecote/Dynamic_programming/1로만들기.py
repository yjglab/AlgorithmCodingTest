n = int(input())
d = [0] * (n + 1)
d[2] = 1
# 0 1 2 3 4 5 6 7
# 0 0 1 2 2 1 2 3
# d[i] = min(d[i - 1] + 1, d[i // 2], d[i // 3], d[i // 5])
for i in range(3, n + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)
    
print(d[n])