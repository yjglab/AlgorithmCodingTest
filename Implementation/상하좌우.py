n = int(input())
move_lst = list(input().split())
x, y = 0, 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
move_direction = ["U", "D", "L", "R"]
for move in move_lst:
    nx, ny = 0, 0
    for i in range(4):
        if move == move_direction[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 0 or ny < 0 or nx >= n or ny >= n:
        continue
    x, y = nx, ny
print(x + 1, y + 1)