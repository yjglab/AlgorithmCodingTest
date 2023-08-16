function sol2573(n: number, m: number, arr: Array<Array<number>>) {
  const dfs = (r: number, c: number, vst: Array<Array<number>>) => {
    if (vst[r][c]) return 0;
    vst[r][c] = 1;
    for (const d of dist) {
      const [dr, dc] = [r + d[0], c + d[1]];
      if (dr < 0 || dc < 0 || dr >= n || dc >= m) continue;
      if (!vst[dr][dc]) dfs(dr, dc, vst);
    }
    return 1;
  };
  const dist = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];
  let result = 0;
  while (1) {
    const q = [];
    const vst = Array.from({ length: n }, () => Array(m).fill(1));
    let front = 0;

    for (let i = 0; i < n; i += 1) {
      for (let j = 0; j < m; j += 1) {
        if (arr[i][j]) {
          vst[i][j] = 0;
          q.push([i, j]);
        }
      }
    }
    if (!q[front + 1]) return 0;
    let f = 0;
    for (let i = 0; i < n; i += 1) {
      for (let j = 0; j < m; j += 1) {
        f += dfs(i, j, vst);
        if (f == 2) return result;
      }
    }
    const cand = [];
    while (q[front]) {
      const [qr, qc] = q[front++];
      let cnt = 0;
      for (const d of dist) {
        const [dr, dc] = [qr + d[0], qc + d[1]];
        if (dr < 0 || dc < 0 || dr >= n || dc >= m) continue;
        if (!arr[dr][dc]) cnt += 1;
      }
      if (cnt) cand.push([qr, qc, cnt]);
    }
    cand.forEach((cd) => {
      const [r, c, v] = cd;
      if (arr[r][c] - v < 0) arr[r][c] = 0;
      else arr[r][c] -= v;
    });
    result += 1;
    if (!cand[0]) return 0;
  }
}

console.log(
  sol2573(5, 7, [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 3, 6, 0, 6, 7, 0],
    [0, 3, 0, 0, 0, 10, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
  ])
);
