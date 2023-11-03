function solution(r, c, k, arr) {
  let result = 0;
  const visited = Array.from({ length: r }, () => Array(c).fill(0));
  const dir = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];
  const [tr, tc] = [0, c - 1];
  const dfs = (sr, sc, cnt) => {
    visited[sr][sc] = 1;
    if (cnt > k) return;
    if (sr === tr && sc === tc && cnt === k) return (result += 1);
    for (const d of dir) {
      const [dr, dc] = [sr + d[0], sc + d[1]];
      if (dr < 0 || dc < 0 || dr >= r || dc >= c) continue;
      if (arr[dr][dc] === "T") continue;
      if (!visited[dr][dc]) {
        visited[dr][dc] = 1;
        dfs(dr, dc, cnt + 1);
        visited[dr][dc] = 0;
      }
    }
  };
  dfs(r - 1, 0, 1);
  return result;
}
console.log(
  solution(3, 4, 6, [
    [".", ".", ".", "."],
    [".", "T", ".", "."],
    [".", ".", ".", "."],
  ])
);
