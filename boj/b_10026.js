function solution(n, strings) {
  const [arr1, arr2] = [[], []];
  for (const s of strings) {
    arr1.push(s.split(""));
    arr2.push(s.replaceAll("R", "G").replaceAll("G", "R").split(""));
  }
  const dist = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];
  const visited1 = Array.from({ length: n }, () => Array(n).fill(0));
  const visited2 = Array.from({ length: n }, () => Array(n).fill(0));

  const dfs = (r, c, v, arr, visited) => {
    if (visited[r][c]) return false;
    if (arr[r][c] == v) {
      visited[r][c] = 1;
      for (const d of dist) {
        const [nr, nc] = [r + d[0], c + d[1]];
        if (nr < 0 || nc < 0 || nr >= n || nc >= n) continue;
        dfs(nr, nc, v, arr, visited);
      }
    }
    return true;
  };
  let [r1, r2] = [0, 0];
  for (let i = 0; i < n; i += 1) {
    for (let j = 0; j < n; j += 1) {
      r1 += dfs(i, j, arr1[i][j], arr1, visited1);
      r2 += dfs(i, j, arr2[i][j], arr2, visited2);
    }
  }
  return [r1, r2];
}

console.log(solution(5, ["RRRBB", "GGBBB", "BBBRR", "BBRRR", "RRRRR"]));
