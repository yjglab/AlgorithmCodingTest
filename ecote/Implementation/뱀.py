from collections import deque

n = int(input())
arr = [[0] * n for _ in range(n)]
k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    arr[x - 1][y - 1] = 1
l = int(input())
action = deque()
for _ in range(l):
    x, c = input().split()
    action.append((int(x), c))

def rotate(d, act_d): # "UP", "RIGHT", "DOWN", "LEFT" 0 1 2 3
    return (d + 1) % 4 if act_d == "D" else (d + 3) % 4

def move(hq, tq, dx, dy):
    hx, hy = hq.popleft()
    if hx + dx >= n or hx + dx < 0 or hy + dy >= n or hy + dy < 0: # 맵 바깥이라면
        return False
    hq.append((hx + dx, hy + dy))
    tq.append((hx, hy))
    if arr[hx + dx][hy + dy] == 7:  # 자신이라면
        return False
    elif arr[hx + dx][hy + dy] == 1:  # 사과라면
        pass
    else:
        tx, ty = tq.popleft()
        arr[tx][ty] = 0

    arr[hx + dx][hy + dy] = 7
    return True

def start(arr):
    hq, tq = deque(), deque() # 머리 큐, 꼬리 큐
    hq.append((0, 0))
    d, t = 1, 0 # 시작 방향, 시작 시간
    arr[0][0] = 7 # 뱀 시작 위치
    act_clear, act_time, act_d = True, None, None # 액션 가능, 시간, 회전방향

    while True:
        t += 1
        if d == 0: # 위쪽
            if not move(hq, tq, -1, 0): # 움직일 때 조건에 걸린다면 종료
                return t
        elif d == 1: # 오른쪽
            if not move(hq, tq, 0, 1):
                return t
        elif d == 2: # 아래쪽
            if not move(hq, tq, 1, 0):
                return t
        elif d == 3: # 왼쪽
            if not move(hq, tq, 0, -1):
                return t
        if action and act_clear: # 액션이 존재하고 꺼낼 수 있는 상황이면
            act_time, act_d = action.popleft()
            act_clear = False
        if t == act_time:
            d = rotate(d, act_d)
            act_clear = True

print(start(arr))