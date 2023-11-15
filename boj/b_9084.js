function solution(t, cases) {
  for (let _ = 0; _ < t; _ += 1) {
    const [n, coins, m] = cases[_];
    coins.unshift(0);
    const table = Array.from({ length: n + 1 }, () => Array(m + 1).fill(0));
    for (let i = 1; i <= n; i += 1) table[i][0] = 1;
    for (let i = 1; i <= n; i += 1) {
      const coin = coins[i];
      for (let j = 1; j <= m; j += 1) {
        table[i][j] += table[i - 1][j];
        if (j - coin >= 0) table[i][j] += table[i][j - coin];
      }
    }
    console.log(table[n][m]);
  }
}

solution(3, [
  [2, [1, 2], 1000],
  [3, [1, 5, 10], 100],
  [2, [5, 7], 22],
]);
