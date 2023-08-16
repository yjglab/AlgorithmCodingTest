function solution(arrays) {
  for (const arr of arrays) {
    if (arr[0] === "0") return;
    arr.shift();
    const combinations = (arr, n) => {
      const result = [];
      if (n === 1) return arr.map((value) => [value]);

      arr.forEach((fixed, index, origin) => {
        const rest = origin.slice(index + 1);
        const combs = combinations(rest, n - 1);
        const attached = combs.map((comb) => [fixed, ...comb]);
        result.push(...attached);
      });
      return result;
    };
    for (const res of combinations(arr, 6)) console.log(res.join(" "));
    console.log();
  }
}
solution([
  ["7", "1", "2", "3", "4", "5", "6", "7"],
  ["8", "1", "2", "3", "5", "8", "13", "21", "34"],
  ["0"],
]);

function solution(arrays) {
  for (const arr of arrays) {
    if (arr[0] === "0") return;
    arr.shift();

    const dfs = (s) => {
      if (s.length === 6) return console.log(s.join(" "));

      for (const i of arr) {
        if (!s.length) {
          s.push(i);
          dfs(s);
          s.pop();
        } else if (parseInt(s[s.length - 1]) < parseInt(i)) {
          s.push(i);
          dfs(s);
          s.pop();
        }
      }
    };
    dfs([]);
    console.log();
  }
}
solution([
  ["7", "1", "2", "3", "4", "5", "6", "7"],
  ["8", "1", "2", "3", "5", "8", "13", "21", "34"],
  ["0"],
]);
