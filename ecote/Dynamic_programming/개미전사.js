let n = parseInt(prompt());
let foods = prompt()
  .split(" ")
  .map((v) => parseInt(v));
let d = Array(n).fill(0);
d[1] = Math.max(d[0], foods[1]);
for (let i = 2; i <= n; i += 1) {
  d[i] = Math.max(d[i - 1], foods[i] + d[i - 2]);
}
console.log(d[n - 1]);
