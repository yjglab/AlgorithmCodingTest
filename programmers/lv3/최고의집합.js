function solution(n, s) {
  if (!parseInt(s / n)) return [-1];
  const arr = Array(n).fill(parseInt(s / n));
  for (let i = 0; i < s % n; i += 1) arr[i] += 1;
  arr.sort();
  return arr;
}
