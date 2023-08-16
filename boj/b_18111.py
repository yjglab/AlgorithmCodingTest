import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, m, inven = map(int, input().split())
arr = []
for i in range(n):
    arr.extend(list(map(int, input().split())))
arr.sort(reverse=1)
s, e = min(arr), max(arr)
result = []
for k in range(s, e + 1):
    t, b, stop = 0, inven, 0
    for v in arr:
        if v > k:
            b += v - k
            t += (v - k) * 2
        elif v < k:
            if b - (k - v) >= 0:
                b -= k - v
                t += k - v
            else:
                stop = 1
                break
    if not stop:
        result.append((t, k))
if not result:
    print(0, e)
else:
    print(*sorted(result, key=lambda x: (x[0], -x[1]))[0])
