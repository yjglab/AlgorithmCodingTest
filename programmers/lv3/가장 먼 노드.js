function solution(n, edge) {
  const graph = Array.from({ length: n + 1 }, () => []);
  edge.forEach((e) => {
    const [a, b] = e;
    graph[a].push(b);
    graph[b].push(a);
  });
  const q = [[1, -1]];
  const visited = Array(n + 1).fill(0);
  visited[1] = 1;
  const result = Array(n + 1).fill(0);
  while (q.length) {
    const [now, cnt] = q.shift();
    result[now] += cnt + 1;
    for (const i of graph[now]) {
      if (!visited[i]) {
        visited[i] = 1;
        q.push([i, cnt + 1]);
      }
    }
  }
  const m = Math.max(...result);
  let cnt = 0;
  result.forEach((v) => {
    if (v === m) cnt += 1;
  });
  return cnt;
}
