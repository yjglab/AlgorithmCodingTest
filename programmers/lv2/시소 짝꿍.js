function solution(weights) {
  let result = 0;
  const table = Array(4001).fill(0);
  const isInt = (n) => (n % 1 === 0 ? n : 0);
  weights.forEach((w) => {
    result += table[w] + table[w * 2];
    if (isInt(w / 2)) result += table[w / 2];
    if (isInt((w * 2) / 3)) result += table[(w * 2) / 3];
    if (isInt((w * 3) / 2)) result += table[(w * 3) / 2];
    if (isInt((w * 4) / 3)) result += table[(w * 4) / 3];
    if (isInt((w * 3) / 4)) result += table[(w * 3) / 4];
    table[w] += 1;
  });
  return result;
}
