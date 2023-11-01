function solution(n, edges) {
  const arr = Array.from({ length: n }, () => Array(n).fill(n));
  const dist = Array(n).fill(0);
  for (let i = 0; i < n; i += 1) {
    for (let j = 0; j < n; j += 1) {
      if (i === j) arr[i][j] = 0;
    }
  }
  edges.forEach((edge) => {
    const [a, b] = edge;
    arr[a - 1][b - 1] = 1;
    arr[b - 1][a - 1] = 1;
  });
  for (let k = 0; k < n; k += 1) {
    for (let i = 0; i < n; i += 1) {
      for (let j = 0; j < n; j += 1) {
        arr[i][j] = Math.min(arr[i][j], arr[i][k] + arr[k][j]);
      }
    }
  }
  for (let i = 0; i < n; i += 1) dist[i] = Math.max(...arr[i]);
  const t = Math.min(...dist);
  const result = [[t, 0], []];
  for (let i = 0; i < n; i += 1) {
    if (dist[i] == t) {
      result[0][1] += 1;
      result[1].push(i + 1);
    }
  }
  return result;
}
console.log(
  solution(5, [
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [2, 4],
    [5, 3],
  ])
);
