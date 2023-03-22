function solution(m, n, board) {
  board = board.map((v) => v.split(""));
  let result = 0;
  while (1) {
    const willRemove = [];
    for (let i = 0; i < m - 1; i += 1) {
      for (let j = 0; j < n - 1; j += 1) {
        if (
          board[i][j] &&
          board[i][j] === board[i][j + 1] &&
          board[i][j] === board[i + 1][j] &&
          board[i][j] === board[i + 1][j + 1]
        ) {
          willRemove.push([i, j]);
        }
      }
    }
    willRemove.forEach((v) => {
      const [x, y] = v;
      board[x][y] = 0;
      board[x][y + 1] = 0;
      board[x + 1][y] = 0;
      board[x + 1][y + 1] = 0;
    });

    for (let i = m - 1; i > 0; i -= 1) {
      for (let j = 0; j < n; j += 1) {
        if (!board[i][j]) {
          let f = i - 1;
          while (f >= 0) {
            if (board[f][j]) {
              board[i][j] = board[f][j];
              board[f][j] = 0;
              break;
            } else {
              f -= 1;
            }
          }
        }
      }
    }
    if (!willRemove.length) return board.flat().filter((v) => !v).length;
  }
}
