let input = prompt()
  .split(" ")
  .map((v) => parseInt(v));
let n = input[0];
let m = input[1];

let parent = Array(n + 1).fill(0);
for (let i = 1; i < n + 1; i += 1) {
  parent[i] = i;
}
const findParent = (parent, x) => {
  if (parent[x] != x) {
    parent[x] = findParent(parent, parent[x]);
  }
  return parent[x];
};
const unionParent = (parent, a, b) => {
  a = findParent(parent, a);
  b = findParent(parent, b);
  a < b ? (parent[b] = a) : (parent[a] = b);
};
for (let _ = 0; _ < n + 1; _ += 1) {
  let input = prompt()
    .split(" ")
    .map((v) => parseInt(v));
  let sig = input[0];
  let a = input[1];
  let b = input[2];

  if (sig == 1) {
    if (findParent(parent, a) == findParent(parent, b)) {
      console.log("YES");
    } else {
      console.log("NO");
    }
  } else if (sig == 0) {
    unionParent(parent, a, b);
  }
}
