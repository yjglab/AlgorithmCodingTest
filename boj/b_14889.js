function solution(n, arr) {
  arr.forEach((v) => v.unshift(0));
  arr.unshift(Array(n + 1).fill(0));
  let result = 101;
  const visited = Array(n + 1).fill(0);
  const dfs = (v, a) => {
    if (a.length === parseInt(n / 2)) {
      const b = [];
      for (let k = 1; k <= n; k += 1) {
        if (!visited[k]) b.push(k);
      }
      let [t1, t2] = [0, 0];
      for (let i = 0; i < parseInt(n / 2); i += 1) {
        for (let j = 0; j < parseInt(n / 2); j += 1) {
          if (i !== j) {
            t1 += arr[a[i]][a[j]];
            t2 += arr[b[i]][b[j]];
          }
        }
      }
      result = Math.min(result, Math.abs(t1 - t2));
      return;
    }
    for (let i = v + 1; i <= n; i += 1) {
      if (!visited[i]) {
        visited[i] = 1;
        a.push(i);
        dfs(i, a);
        a.pop();
        visited[i] = 0;
      }
    }
  };
  for (let i = 1; i < parseInt(n / 2); i += 1) {
    visited[i] = 1;
    dfs(i, [i]);
    visited[i] = 0;
  }
  return result;
}
solution(6, [
  [0, 1, 2, 3, 4, 5],
  [1, 0, 2, 3, 4, 5],
  [1, 2, 0, 3, 4, 5],
  [1, 2, 3, 0, 4, 5],
  [1, 2, 3, 4, 0, 5],
  [1, 2, 3, 4, 5, 0],
]);
