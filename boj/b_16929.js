function solution(n, m, arr) {
  let result = 0;
  const visited = Array.from({ length: n }, () => Array(m).fill(0));
  const dfs = (r, c, sr, sc, s, cnt) => {
    for (const d of [
      [-1, 0],
      [1, 0],
      [0, -1],
      [0, 1],
    ]) {
      const [nr, nc] = [r + d[0], c + d[1]];
      if (cnt >= 4 && nr == sr && nc == sc) return (result = 1);
      if (nr < 0 || nc < 0 || nr >= n || nc >= m) continue;
      if (!visited[nr][nc] && arr[nr][nc] === s) {
        visited[nr][nc] = 1;
        dfs(nr, nc, sr, sc, s, cnt + 1);
        visited[nr][nc] = 0;
      }
    }
  };
  for (let i = 0; i < n; i += 1) {
    for (let j = 0; j < m; j += 1) {
      if (result) return "Yes";
      visited[i][j] = 1;
      dfs(i, j, i, j, arr[i][j], 1);
      visited[i][j] = 0;
    }
  }
  return "No";
}

console.log(
  solution(3, 4, [
    ["A", "A", "A", "A"],
    ["A", "B", "C", "A"],
    ["A", "A", "A", "A"],
  ])
);
console.log(
  solution(3, 4, [
    ["A", "A", "A", "A"],
    ["A", "B", "C", "A"],
    ["A", "A", "D", "A"],
  ])
);
console.log(
  solution(4, 4, [
    ["Y", "Y", "Y", "R"],
    ["B", "Y", "B", "Y"],
    ["B", "B", "B", "Y"],
    ["B", "B", "B", "Y"],
  ])
);
console.log(
  solution(7, 6, [
    ["A", "A", "A", "A", "A", "B"],
    ["A", "B", "B", "B", "A", "B"],
    ["A", "B", "A", "A", "A", "B"],
    ["A", "B", "A", "B", "B", "B"],
    ["A", "B", "A", "A", "A", "B"],
    ["A", "B", "B", "B", "A", "B"],
    ["A", "A", "A", "A", "A", "B"],
  ])
);
console.log(
  solution(2, 13, [
    ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
    ["N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"],
  ])
);
