function solution(n, arr) {
  let arr_s = [...arr].sort((a, b) => a - b);
  let [table, cnt] = [{}, -1];
  for (let i = 0; i < n; i += 1) {
    if (table[arr_s[i]] === undefined) table[arr_s[i]] = ++cnt;
  }
  const result = [];
  arr.forEach((a) => result.push(table[a]));
  return result;
}

console.log(solution(6, [2, 3, 0, 3, 1]));
