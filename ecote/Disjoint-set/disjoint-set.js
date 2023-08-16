const find_parent = (parent, x) => {
  if (parent[x] != x) {
    parent[x] = find_parent(parent, parent[x]);
  }
  return parent[x];
};
const union_parent = (parent, a, b) => {
  a = find_parent(parent, a);
  b = find_parent(parent, b);
  if (a < b) {
    parent[b] = a;
  } else {
    parent[a] = b;
  }
};

let input = prompt()
  .split(" ")
  .map((v) => parseInt(v));
let v = input[0];
let e = input[1];

let parent = Array(v + 1).fill(0);
for (let i = 1; i < v + 1; i += 1) {
  parent[i] = i;
}
let cycle = false;
for (let i = 0; i < e; i += 1) {
  let input = prompt()
    .split(" ")
    .map((v) => parseInt(v));
  let a = input[0];
  let b = input[1];
  if (find_parent(parent, a) === find_parent(parent, b)) {
    cycle = true;
    break;
  } else {
    union_parent(parent, a, b);
  }
}
if (cycle) console.log("cycle");
else console.log("not cycle");
