function solution(board, moves) {
  const stk = [];
  let result = 0;
  moves.forEach((c) => {
    for (let i = 0; i < board[0].length; i += 1) {
      if (board[i][c - 1]) {
        stk.push(board[i][c - 1]);
        board[i][c - 1] = 0;
        break;
      }
    }
    for (let i = 1; i < stk.length; i += 1) {
      if (stk[i] === stk[i - 1]) {
        stk.splice(i - 1, 2);
        i -= 2;
        result += 2;
      }
    }
  });
  return result;
}
