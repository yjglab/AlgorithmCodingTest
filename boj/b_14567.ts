function sol14567(n: number, m: number, numbers: Array<Array<number>>) {
  const indegree = Array(n + 1).fill(0);
  const graph: number[][] = Array.from({ length: n + 1 }, () => []);
  numbers.forEach((v) => {
    const [a, b] = v;
    graph[a].push(b);
    indegree[b] += 1;
  });
  const q: Array<Array<number>> = [];
  let front = 0;
  const result = Array(n + 1).fill(0);
  for (let i = 1; i <= n; i += 1) {
    if (!indegree[i]) q.push([i, 1]);
  }
  while (q[front]) {
    const [now, r] = q[front++];
    result[now] = r;
    graph[now].forEach((v) => {
      indegree[v] -= 1;
      if (!indegree[v]) q.push([v, r + 1]);
    });
  }
  console.log(result.slice(1));
}
sol14567(6, 4, [
  [1, 2],
  [1, 3],
  [2, 5],
  [4, 5],
]);
