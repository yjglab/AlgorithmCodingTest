function solution(n, list) {
  const graph = Array.from({ length: n + 1 }, () => []);
  const cycle = Array(n + 1).fill(3000);
  const visited = Array(n + 1).fill(0);
  let finded = 0;

  list.forEach((v) => {
    graph[v[0]].push(v[1]);
    graph[v[1]].push(v[0]);
  });

  const findCycle = (passed) => {
    if (finded) return;
    for (const v of graph[passed[passed.length - 1]]) {
      if (v === passed[0] && passed.length >= 3)
        return (finded = 1 && passed.forEach((p) => (cycle[p] = 0)));
      if (!visited[v]) {
        visited[v] = 1;
        findCycle(passed.concat(v));
        visited[v] = 0;
      }
    }
  };

  for (let i = 1; i <= n; i += 1) {
    if (!finded) {
      visited[i] = 1;
      findCycle([i]);
      visited[i] = 0;
    }
  }
  let [q, front] = [[], 0];
  for (let i = 1; i <= n; i += 1) if (!cycle[i]) q.push([i, 1]);
  while (front <= q.length - 1) {
    let [now, d] = q[front++];
    for (const v of graph[now]) {
      if (cycle[v] === 3000) {
        cycle[v] = d;
        q.push([v, d + 1]);
      }
    }
  }
  return cycle.slice(1);
}

console.log(
  solution(12, [
    [1, 3],
    [3, 4],
    [4, 5],
    [5, 6],
    [6, 7],
    [7, 8],
    [8, 4],
    [2, 3],
    [7, 9],
    [9, 12],
    [7, 10],
    [10, 11],
  ])
);
console.log(
  solution(6, [
    [1, 2],
    [3, 4],
    [6, 4],
    [2, 3],
    [1, 3],
    [3, 5],
  ])
);
