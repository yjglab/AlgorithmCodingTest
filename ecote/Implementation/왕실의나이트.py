ipt = list(input())
dx = [-2, -2, -1, -1, 2, 2, 1, 1]
dy = [-1, 1, -2, 2, -1, 1, -2, 2]
x = ord(ipt[0]) - 96
y = int(ipt[1])
cnt = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx <= 0 or ny <= 0 or nx > 8 or ny > 8:
        continue
    cnt += 1
print(cnt)