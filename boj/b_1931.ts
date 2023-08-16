function sol1931(n: number, arr: Array<Array<number>>) {
  arr.sort((a, b) => a[1] - b[1] || a[0] - b[0]);
  let [now, result] = [arr[0], 1];
  for (let i = 1; i < n; i += 1) {
    if (arr[i][0] >= now[1]) [now, result] = [arr[i], result + 1];
  }
  console.log(result);
}
sol1931(11, [
  [1, 4],
  [3, 5],
  [0, 6],
  [5, 7],
  [3, 8],
  [5, 9],
  [6, 10],
  [8, 11],
  [8, 12],
  [2, 13],
  [12, 14],
]);
