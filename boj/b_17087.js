function solution(n, s, arr) {
  const gcd = (a, b) => (a % b === 0 ? b : gcd(b, a % b));
  arr.push(s);
  arr.sort((a, b) => a - b);
  let result = arr[1] - arr[0];
  for (let i = 2; i <= n; i += 1) {
    result = gcd(result, arr[i] - arr[i - 1]);
  }
  return result;
}
console.log(solution(3, 81, [33, 105, 57]));
console.log(solution(3, 3, [1, 7, 11]));
