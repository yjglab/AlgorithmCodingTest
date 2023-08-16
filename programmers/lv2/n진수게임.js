function solution(n, t, m, p) {
  let [converted, result] = ["", ""];
  for (let i = 0; i < t * m; i += 1) converted += i.toString(n);
  for (let i = p - 1; i < t * m; i += m) result += converted[i];
  return result.toUpperCase();
}
