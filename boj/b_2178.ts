function sol2178(n: number, m: number, arr: Array<string>) {
  const sarr = arr.map((v) => v.split("").map((m) => parseInt(m)));
  const dist = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];
  const q = [[0, 0]];
  let front = 0;
  while (q[front]) {
    const [qr, qc] = q[front++];
    for (const d of dist) {
      const [dr, dc] = [qr + d[0], qc + d[1]];
      if (dr < 0 || dc < 0 || dr >= n || dc >= m) continue;
      if (sarr[dr][dc] === 1) {
        sarr[dr][dc] = sarr[qr][qc] + 1;
        q.push([dr, dc]);
      }
    }
  }
  console.log(sarr[n - 1][m - 1]);
}

sol2178(4, 6, ["101111", "101010", "101011", "111011"]);
