function solution(numbers, target) {
  let result = 0;
  const dfs = (idx, accr) => {
    if (idx === numbers.length) return accr === target ? ++result : 1;
    dfs(idx + 1, accr + numbers[idx]);
    dfs(idx + 1, accr - numbers[idx]);
  };
  return dfs(0, 0) || result;
}
