function solution(n, arr) {
  const table = Array(Math.max(...arr) + 1).fill([]);
  arr.forEach((v) => {
    const targetScope = table.slice(0, v);
    const targetLens = targetScope.map((v) => v.length);
    table[v] = table[targetLens.indexOf(Math.max(...targetLens))].concat(v);
  });
  const resultLens = table.map((v) => v.length);
  const resultIdx = resultLens.indexOf(Math.max(...resultLens));
  return [table[resultIdx].length, table[resultIdx]];
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
