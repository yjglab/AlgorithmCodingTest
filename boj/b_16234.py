import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0
dir = ((-1, 0), (1, 0), (0, -1), (0, 1))
from collections import deque

# 연합 후보 위치 탐색
def transfer(sr, sc, visited):
    q = deque()
    q.append((sr, sc))
    targets = [(sr, sc)] # 연합할 타겟 좌표들
    targets_sum = arr[sr][sc] # 연합 인구 합
    while q:
        qr, qc = q.popleft()
        for [x, y] in dir:
            dr, dc = qr + x, qc + y
            # 맵 밖이거나 이미 방문한 경우
            if dr < 0 or dc < 0 or dr >= n or dc >= n:
                continue
            if visited[dr][dc]:
                continue
            diff = abs(arr[qr][qc] - arr[dr][dc])
            # 탐색 위치와 현재 위치와의 절댓값이 L이상 R이하이면 타겟 좌표로 등록
            if diff >= l and diff <= r:
                visited[dr][dc] = 1
                targets.append((dr, dc))
                targets_sum += arr[dr][dc]
                q.append((dr, dc))
    return [targets, targets_sum]

# 이동 횟수 카운트
while 1:
    visited = [[0] * n for _ in range(n)]
    candidates = [] # 연합에 넣을 좌표 후보
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = 1
                targets, targets_sum = transfer(i, j, visited) # 연합할 타겟 좌표들, 연합 인구 합
                # 2곳 이상의 연합이 생기면 후보에 넣음
                if len(targets) > 1:
                    candidates.append([targets, targets_sum])
    # 후보가 없을 경우 종료
    if not candidates:
        print(result)
        break
    for [targets, target_sum] in candidates:
        size = target_sum // len(targets) # 연합 인구 수 평균
        for [tr, tc] in targets:
            arr[tr][tc] = size
    result += 1
