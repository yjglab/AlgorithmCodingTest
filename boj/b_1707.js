function solution(v, e, edges) {
  const bfs = (s, marks) => {
    const q = [[s, true]];
    let front = 0;
    marks[s] = true;
    while (q[front]) {
      const [now, m] = q[front++];
      for (const v of graph[now]) {
        if (marks[v] === m) return false;
        else if (marks[v] === -1) {
          marks[v] = !m;
          q.push([v, !m]);
        }
      }
    }
    return true;
  };
  const graph = Array.from({ length: v + 1 }, () => []);
  const marks = Array(v + 1).fill(-1);
  edges.forEach((edge) => {
    const [a, b] = edge;
    graph[a].push(b);
    graph[b].push(a);
  });
  let result = "YES";
  for (let i = 1; i <= v; i += 1) {
    if (graph[i] && marks[i] === -1 && !bfs(i, marks)) {
      result = "NO";
      break;
    }
  }
  return result;
}

solution(4, 4, [
  [1, 2],
  [2, 3],
  [3, 4],
  [4, 2],
]);
solution(5, 4, [
  [1, 2],
  [3, 4],
  [3, 5],
  [4, 5],
]);
solution(5, 3, [
  [2, 4],
  [3, 5],
  [4, 5],
]);
