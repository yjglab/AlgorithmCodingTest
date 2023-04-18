function solution(n, numbers) {
  const result = Array(n).fill(-1);
  const s = [];
  numbers.forEach((number, i) => {
    while (s.length && s[s.length - 1][0] < number) {
      const [v, idx] = s.pop();
      result[idx] = number;
    }
    s.push([number, i]);
  });
  return result;
}
console.log(solution(5, [7, 8, 10, 12, 1]));
