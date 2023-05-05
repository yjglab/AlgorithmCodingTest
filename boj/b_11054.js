function solution(n, array) {
  const [tableA, tableB] = [Array(n).fill(1), Array(n).fill(1)];
  for (let i = 0; i < n; i += 1) {
    for (let j = 0; j < i; j += 1) {
      if (array[i] > array[j]) tableA[i] = Math.max(tableA[i], tableA[j] + 1);
    }
  }
  for (let i = n - 1; i >= 0; i -= 1) {
    for (let j = n - 1; j > i; j -= 1) {
      if (array[i] > array[j]) tableB[i] = Math.max(tableB[i], tableB[j] + 1);
    }
  }
  let result = 0;
  for (let i = 0; i < n; i += 1) {
    result = Math.max(result, tableA[i] + tableB[i] - 1);
  }
  return result;
}
console.log(solution(10, [1, 5, 2, 1, 4, 3, 4, 5, 2, 1]));
