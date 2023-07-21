function sol11660(n: number, m: number, inputs: Array<Array<number>>) {
  const arr = inputs.slice(0, n);
  const targets = inputs.slice(n, n + m);
  const d = Array.from({ length: n + 1 }, () => Array(n + 1).fill(0));

  for (let i = 1; i <= n; i += 1) {
    for (let j = 1; j <= n; j += 1) {
      d[i][j] = arr[i - 1][j - 1] + d[i - 1][j] + d[i][j - 1] - d[i - 1][j - 1];
    }
  }
  targets.forEach((v) => {
    const [x1, y1, x2, y2] = v;
    console.log(d[x2][y2] + d[x1 - 1][y1 - 1] - d[x2][y1 - 1] - d[x1 - 1][y2]);
  });
}

sol11660(2, 4, [
  [1, 2],
  [3, 4],
  [1, 1, 1, 1],
  [1, 2, 1, 2],
  [2, 1, 2, 1],
  [2, 2, 2, 2],
]);
