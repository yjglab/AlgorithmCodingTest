# n, m = map(int, input().split())
# a, b, direction = map(int, input().split())
# field = []
field = [[1, 1, 1, 1],
         [1, 0, 0, 1],
         [1, 1, 0, 1],
         [1 ,1 ,1 ,1]]
a, b, direction = 1, 1, 0
n, m = 4, 4
#for i in range(n):
    #field.append(list(map(int, input().split())))
da = [-1, 0, 1, 0]
db = [0, 1, 0, -1] # 
cnt = 1

def back(direction, a, b):
    na, nb = a, b
    if direction == 3:
        na, nb = a, b + 1
    elif direction == 2:
        na, nb = a - 1, b
    elif direction == 1:
        na, nb = a, b - 1
    elif direction == 0:
        na, nb = a + 1, b
    if field[na][nb] != 1:
        return na, nb
    elif field[na][nb] == 1:
        return a, b
while True:
    flag = False
    for i in range(3, -1, -1):
        na = a + da[i]
        nb = b + db[i]
        if na >= 0 and nb >- 0 and na < n and nb < m and field[na][nb] not in [1, 2]:
            field[a][b] = 2
            a, b, direction = na, nb, i
            cnt += 1
            flag = True
    if not flag :
        na, nb = back(direction, a, b)
        if a == na and b == nb: # 그대로인 경우
            break
        field[a][b] = 2
        a, b = na, nb
        print(a, b)
    
print(cnt, a, b)

# 2트
n, m = map(int, input().split())
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

x, y, d = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr[x][y] = 2 # 방문 표시
d_cnt = 0
res = 1
while True:
    d = (d + 3) % 4
    nx, ny = x + move[d][0], y + move[d][1]
    if arr[nx][ny] == 0:
        d_cnt = 0
        x, y = nx, ny
        arr[x][y] = 2
        res += 1
    else:
        d_cnt += 1
    if d_cnt == 4:
        
        nd = (d + 2) % 4
        nx, ny = x + move[nd][0], y + move[nd][1]
        if arr[nx][ny] == 1:
            break 
        x, y = nx, ny
        d_cnt = 0
print(res)
