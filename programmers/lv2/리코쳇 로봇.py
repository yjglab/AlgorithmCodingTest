def solution(board):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    br, bc = len(board), len(board[0])
    visited = [[0] * bc for _ in range(br)]
    
    def bfs(sr, sc):
        visited[sr][sc] = 1
        
        from collections import deque
        q = deque([(sr, sc)])
        
        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r, c
                while 1:
                    nr += dr[i]
                    nc += dc[i]
                    if nr < 0 or nc < 0 or nr >= br or nc >= bc:
                        nr -= dr[i]
                        nc -= dc[i]
                        break
                    elif board[nr][nc] == "D":
                        nr -= dr[i]
                        nc -= dc[i]
                        break
                if not visited[nr][nc]:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))
                if board[nr][nc] == "G":
                    return visited[nr][nc]
        return 0
    
    for i in range(len(board)):
        if "R" in board[i]:
            result = bfs(i, board[i].find("R"))
            return result - 1 if result else -1