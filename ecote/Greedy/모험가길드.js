let n = parseInt(prompt());
let arr = prompt()
  .split(" ")
  .map((v) => parseInt(v));
let result = 0,
  cnt = 0,
  box = 0;
for (let x of arr) {
  box = Math.max(x, box);
  cnt += 1;
  if (box === cnt) {
    cnt = 0;
    box = 0;
    result += 1;
  }
}
console.log(result);
