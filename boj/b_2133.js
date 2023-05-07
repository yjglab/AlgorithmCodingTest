function solution(n) {
  const table = Array(n + 1).fill(0);
  table[0] = 1;
  for (let i = 2; i <= n; i += 2) {
    table[i] += table[i - 2] * 3;
    for (let j = 0; j <= i - 4; j += 1) table[i] += table[j] * 2;
  }
  return table[n];
}
console.log(solution(6));
