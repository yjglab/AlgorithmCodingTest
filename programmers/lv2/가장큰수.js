function solution(numbers) {
  if (!numbers.reduce((acc, curr) => acc + curr, 0)) return "0";
  return numbers
    .map((v) => v.toString())
    .sort((p, c) => (p + c > c + p ? -1 : 1))
    .join("");
}
