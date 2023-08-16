let inp = prompt()
  .split(" ")
  .map((v) => parseInt(v));
let n = inp[0];
let m = inp[1];
let inf = 1e9;

let graph = [];
for (let i = 0; i <= n; i += 1) {
  let row = [];
  for (let j = 0; j <= n; j += 1) {
    row.push(inf);
  }
  graph.push(row);
}
for (let _ = 0; _ < m; _ += 1) {
  let inp = prompt()
    .split(" ")
    .map((v) => parseInt(v));
  graph[inp[0]][inp[1]] = inp[2];
}
for (let i = 1; i <= n; i += 1) {
  graph[i][i] = 0;
}
for (let k = 1; k <= n; k += 1) {
  for (let i = 1; i <= n; i += 1) {
    for (let j = 1; j <= n; j += 1) {
      graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j]);
    }
  }
}
console.log(graph);
