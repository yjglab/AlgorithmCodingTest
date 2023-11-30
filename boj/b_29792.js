function solution(n, m, k, dmg, bosses) {
  const result = [];
  const [boss, v] = [[], [0]];
  bosses.forEach(([hp, meso]) => {
    boss.push(hp);
    v.push(meso);
  });
  for (let i = 0; i < n; i += 1) {
    const w = [0];
    for (const hp of boss) {
      let [time, rest] = [parseInt(hp / dmg[i]), hp % dmg[i]];
      if (rest > 0) time += 1;
      w.push(time);
    }
    const table = Array.from({ length: k + 1 }, () => Array(901).fill(0));
    for (let i = 1; i <= k; i += 1) {
      for (let j = 1; j <= 900; j += 1) {
        if (j >= w[i])
          table[i][j] = Math.max(
            table[i - 1][j],
            v[i] + table[i - 1][j - w[i]]
          );
        else table[i][j] = table[i - 1][j];
      }
    }
    result.push(table[k][900]);
  }
  result.reverse();
  let maxResult = 0;
  for (let i = 0; i < m; i += 1) maxResult += result[i];
  console.log(maxResult);
}

solution(
  2,
  2,
  3,
  [10, 20],
  [
    [8999, 10],
    [17999, 100],
    [1, 1],
  ]
);
