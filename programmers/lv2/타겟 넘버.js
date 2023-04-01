function solution(numbers, target) {
  let result = 0;
  const dfs = (idx, accr) => {
    if (idx === numbers.length) {
      if (accr === target) return ++result;
      else return;
    }
    dfs(idx + 1, accr + numbers[idx]);
    dfs(idx + 1, accr - numbers[idx]);
  };
  dfs(0, 0);
  return result;
}
