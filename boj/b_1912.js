function solution2(n, numbers) {
  let [curr, nMax] = [numbers[0], numbers[0]];
  for (let i = 1; i < n; i += 1) {
    curr += numbers[i];
    if (curr > nMax) nMax = curr;
    if (numbers[i] > curr) {
      nMax = Math.max(nMax, numbers[i]);
      curr = numbers[i];
    }
  }
  return nMax;
}
function solution(n, numbers) {
  const table = Array(n).fill(0);
  table[0] = numbers[0];
  for (let i = 1; i < n; i += 1) {
    table[i] = Math.max(numbers[i], table[i - 1] + numbers[i]);
  }
  return Math.max(...table);
}
console.log(
  solution(
    30,
    [
      2, -3, 10, -6, -2, -4, -5, 3, -9, 3, 8, -6, -6, 4, 6, -7, 5, -7, 3, 4, 10,
      0, -3, -6, 6, -9, -7, -10, 0, -2,
    ]
  )
);
