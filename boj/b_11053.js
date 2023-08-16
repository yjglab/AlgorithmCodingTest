function solution(n, arr) {
  const table = Array(Math.max(...arr) + 1).fill(0);
  arr.forEach((v) => {
    table[v] = Math.max(...table.slice(0, v)) + 1;
  });
  return Math.max(...table);
}
console.log(solution(6, [10, 20, 10, 30, 20, 50]));
console.log(
  solution(
    20,
    [
      322, 831, 212, 232, 545, 698, 260, 265, 324, 215, 701, 75, 156, 605, 851,
      993, 425, 887, 691, 593,
    ]
  )
);
