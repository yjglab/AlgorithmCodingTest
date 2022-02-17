n = int(input())
foods = [0] + list(map(int, input().split()))
# 1 3 1 5 3 4  1
# 1 3 3 8 8 12 12 
d = [0] * (n + 1)
d[1], d[2] = foods[1], max(d[1], foods[2])
for i in range(n + 1):
    d[i] = max(d[i - 1], foods[i] + d[i - 2])
print(d[n])