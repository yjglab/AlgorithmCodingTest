function findParent(parent, x) {
  if (parent[x] != x) parent[x] = findParent(parent, parent[x]);
  return parent[x];
}
function unionParent(parent, a, b) {
  a = findParent(parent, a);
  b = findParent(parent, b);
  if (a < b) parent[b] = a;
  else parent[a] = b;
}
let input = prompt()
  .split(" ")
  .map((v) => parseInt(v));
let [n, m] = input;
let parent = Array(n + 1).fill(0);
let edges = [];
for (let i = 1; i < n + 1; i += 1) parent[i] = i;
for (let _ = 0; _ < m; _ += 1) {
  let input = prompt()
    .split(" ")
    .map((v) => parseInt(v));
  let [a, b, c] = input;

  edges.push([c, a, b]);
}
edges.sort();
let result = 0;
let maxLength = 0;
for (let edge of edges) {
  let [c, a, b] = edge;
  if (findParent(parent, a) != findParent(parent, b)) {
    unionParent(parent, a, b);
    result += maxLength = c;
  }
}
console.log(result - maxLength);
