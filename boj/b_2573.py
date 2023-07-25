import sys
sys.stdin = open("input.txt", "r") # 제거
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
import collections
def solution():
    def dfs(r, c, vst):
        if vst[r][c]:
            return 0
        vst[r][c] = 1
        for d in dist:
            dr, dc = r + d[0], c + d[1]
            if dr < 0 or dc < 0 or dr >= n or dc >= m:
                continue
            if not vst[dr][dc]:
                dfs(dr, dc, vst)
        return 1
    dist = ((-1, 0), (1, 0), (0, -1), (0, 1))
    result = 0
    while 1:
        q = collections.deque()
        vst = [[1] * m for _ in range(n)]
        for i in range(n): # 녹지않은 빙산 체크
            for j in range(m):
                if arr[i][j]:
                    vst[i][j] = 0
                    q.append((i, j))
        if len(q) == 1: # 빙산이 1개남은 경우
            return 0
        f = 0 # 종료 플래그
        for i in range(n):
            for j in range(m):
                f += dfs(i, j, vst)
                if f == 2: # 빙산이 나뉘어 있는 경우
                    return result
        cand = [] # 녹아야할 빙산 리스트
        while q:
            qr, qc = q.popleft()
            cnt = 0
            for d in dist:
                dr, dc = qr + d[0], qc + d[1]
                if dr < 0 or dc < 0 or dr >= n or dc >= m:
                    continue
                if not arr[dr][dc]: # 주변 물의 칸 수 체크
                    cnt += 1
            if cnt:
                cand.append((qr, qc, cnt))
        for (r, c, v) in cand: # 빙산 녹이기
            if arr[r][c] - v < 0:
                arr[r][c] = 0
            else:
                arr[r][c] -= v
        result += 1
        if not cand: # 빙산이 다 녹은 경우
            return 0
print(solution())
