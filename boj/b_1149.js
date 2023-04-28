function solution(n, array) {
  const table = Array.from({ length: n }, () => Array(3).fill(0));
  table[0] = [...array[0]];
  for (let i = 1; i < n; i += 1) {
    table[i][0] = array[i][0] + Math.min(table[i - 1][1], table[i - 1][2]);
    table[i][1] = array[i][1] + Math.min(table[i - 1][0], table[i - 1][2]);
    table[i][2] = array[i][2] + Math.min(table[i - 1][0], table[i - 1][1]);
  }
  return Math.min(...table[n - 1]);
}
console.log(
  solution(3, [
    [1, 100, 100],
    [100, 100, 100],
    [1, 100, 100],
  ])
);
