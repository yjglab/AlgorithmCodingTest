function solution(n) {
  if (n === 3) return 1;
  if (n === 4) return -1;
  const table = Array(n + 1).fill(-1);
  [table[3], table[5]] = [1, 1];
  for (let i = 6; i <= n; i += 1) {
    if (table[i - 3] === -1 && table[i - 5] === -1) table[i] = -1;
    else if (table[i - 3] === -1 || table[i - 5] === -1)
      table[i] = Math.max(table[i - 3], table[i - 5]) + 1;
    else table[i] = Math.min(table[i - 3], table[i - 5]) + 1;
  }
  return table[n];
}
console.log(solution(18));
