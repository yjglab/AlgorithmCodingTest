function sol2636(n: number, m: number, arr: Array<Array<number>>) {
  let [result, time] = [0, 0];
  for (const a of arr) {
    result += a.reduce((accr, curr) => accr + curr, 0);
  }
  const dist = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];
  const bfs = () => {
    const visited = Array.from({ length: n }, () => Array(m).fill(0));
    const q = [[0, 0]];
    let front = 0;
    const target = [];
    while (q[front]) {
      const [qr, qc] = q[front++];
      for (const d of dist) {
        const [dr, dc] = [qr + d[0], qc + d[1]];
        if (dr < 0 || dc < 0 || dr >= n || dc >= m || visited[dr][dc]) continue;
        visited[dr][dc] = 1;
        if (!arr[dr][dc]) q.push([dr, dc]);
        else target.push([dr, dc]);
      }
    }
    target.forEach((t) => {
      arr[t[0]][t[1]] = 0;
    });
    return target.length;
  };
  while (1) {
    time += 1;
    const cnt = bfs();
    result -= cnt;
    if (!result) return [time, cnt];
  }
}
console.log(
  sol2636(13, 12, [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  ])
);
