function sol2589(n: number, m: number, arr: Array<string>) {
  const dist = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];
  const bfs = (sr: number, sc: number) => {
    const q: Array<[number, number, number]> = [];
    let front = 0;
    q.push([sr, sc, 0]);
    const times = Array.from({ length: n }, () => Array(m).fill(0));
    times[sr][sc] = 1;
    let t = 0;
    while (q[front]) {
      const [qr, qc, cnt] = q[front++];
      t = cnt + 1;
      for (const d of dist) {
        const [dr, dc]: [number, number] = [qr + d[0], qc + d[1]];
        if (dr < 0 || dc < 0 || dr >= n || dc >= m) continue;
        if (arr[dr][dc] === "L" && times[dr][dc] === 0) {
          times[dr][dc] = cnt + 1;
          q.push([dr, dc, cnt + 1]);
        }
      }
    }
    return t - 1;
  };
  let result = 0;
  for (let i = 0; i < n; i += 1) {
    for (let j = 0; j < m; j += 1) {
      if (arr[i][j] === "L") result = Math.max(result, bfs(i, j));
    }
  }
  return result;
}
console.log(
  sol2589(5, 7, ["WLLWWWL", "LLLWLLL", "LWLWLWW", "LWLWLLL", "WLLWLWW"])
);
