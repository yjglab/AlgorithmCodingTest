function solution(board) {
  const dr = [-1, 1, 0, 0];
  const dc = [0, 0, -1, 1];

  const [br, bc] = [board.length, board[0].length];
  const visited = Array.from({ length: br }, () => Array(bc).fill(0));

  const bfs = (sr, sc) => {
    visited[sr][sc] = 1;
    const q = [[sr, sc]];

    while (q.length) {
      const [r, c] = q.shift();
      for (let i = 0; i < 4; i += 1) {
        let nr = r;
        let nc = c;
        while (1) {
          nr += dr[i];
          nc += dc[i];
          if (
            nr < 0 ||
            nc < 0 ||
            nr >= br ||
            nc >= bc ||
            board[nr][nc] === "D"
          ) {
            nr -= dr[i];
            nc -= dc[i];
            break;
          }
        }
        if (!visited[nr][nc]) {
          visited[nr][nc] = visited[r][c] + 1;
          q.push([nr, nc]);
        }
        if (board[nr][nc] === "G") return visited[nr][nc];
      }
    }
    return 0;
  };
  for (let i = 0; i < br; i += 1) {
    for (let j = 0; j < bc; j += 1) {
      if (board[i][j] === "R") {
        const result = bfs(i, j);
        if (result) return result - 1;
        return -1;
      }
    }
  }
}
