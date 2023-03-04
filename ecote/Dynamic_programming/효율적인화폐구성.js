let inputValue = prompt()
  .split(" ")
  .map((v) => parseInt(v)); // "2 15"
let n = inputValue[0];
let m = inputValue[1];
let money = [];
for (let _ = 0; _ < n; _ += 1) {
  money.push(parseInt(prompt()));
}
let d = Array(10001).fill(10000);
d[0] = 0;
// money 3 5 7
for (let i = 0; i < n; i += 1) {
  for (let j = money[i]; j <= m; j += 1) {
    if (d[j - money[i]] !== 10000) {
      d[j] = Math.min(d[j], d[j - money[i]] + 1);
    }
    console.log(d[j]);
  }
}
console.log(d[m] !== 10000 ? d[m] : -1);
