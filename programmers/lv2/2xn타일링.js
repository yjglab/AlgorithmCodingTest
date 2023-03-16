function solution(n) {
  const arr = [...Array(n)].map((v, i) => i);
  for (let i = 4; i <= n; i += 1)
    arr[i] = (arr[i - 1] + arr[i - 2]) % 1000000007;
  return arr[n];
}
