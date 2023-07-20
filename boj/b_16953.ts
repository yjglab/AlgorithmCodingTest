function sol16953(a: number, b: number) {
  let result = Number.MAX_SAFE_INTEGER;
  const dfs = (n: number, c: number) => {
    if (n > b) return;
    if (n == b) return (result = Math.min(result, c));
    dfs(n * 2, c + 1), dfs(+("" + n + "1"), c + 1);
  };
  dfs(a, 1);
  console.log(result === Number.MAX_SAFE_INTEGER ? -1 : result);
}
sol16953(100, 40021);
