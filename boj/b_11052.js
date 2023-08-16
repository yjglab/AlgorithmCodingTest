function solution(n, cards) {
  table = Array(n + 1).fill(0);
  for (let i = 1; i <= n; i += 1) {
    table[i] = cards[i - 1];
    for (let j = 1; j <= i; j += 1) {
      table[i] = Math.max(table[i], table[j] + table[i - j]);
      if (i % j === 0) {
        table[i] = Math.max(table[i], cards[j - 1] * parseInt(i / j));
      }
    }
  }
  return table[n];
}
console.log(solution(10, [1, 100, 160, 1, 1, 1, 1, 1, 1, 1]));
