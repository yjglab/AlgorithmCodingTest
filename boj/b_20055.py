import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

t = 0
n, k = map(int, input().split())
db = list(map(int, input().split()))
belt = []
for i in db:
    belt.append([i, 0])
def rotate(b):
    r = b.pop()
    b.insert(0, r)
    if b[n - 1][1]:
        b[n - 1][1] = 0
res = 0
while 1:
    t += 1
    rotate(belt)
    for i in range(n - 2, -1, -1):
        if belt[i][1] and belt[i + 1][0] and not belt[i + 1][1]:
            belt[i][1] = 0
            belt[i + 1][1] = 1
            belt[i + 1][0] -= 1
            if i + 1 == n - 1:
                belt[i + 1][1] = 0
            if belt[i + 1][0] == 0:
                res += 1
    if belt[0][0]:
        belt[0][1] = 1
        belt[0][0] -= 1
        if belt[0][0] == 0:
            res += 1
    if res >= k:
        print(t)
        break
