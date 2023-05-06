function solution(n, array) {
  const [tableA, tableB] = [[...array], [...array]];
  for (let i = 1; i < n; i += 1) {
    tableA[i] = Math.max(tableA[i], tableA[i] + tableA[i - 1]);
    tableB[i] = Math.max(tableA[i - 1], tableB[i] + tableB[i - 1]);
  }
  const [a, b] = [Math.max(...tableA), Math.max(...tableB)];
  console.log(a, b);
  return a > b ? a : b;
}
console.log(solution(10, [10, -4, 3, 1, 5, 6, -35, 12, 21, -1]));
