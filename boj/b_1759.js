function solution(l, c, arr) {
  const dfs = (s) => {
    if (s.length === l) {
      let [a, b] = [0, 0];
      for (const m of s) "aeiou".includes(m) ? (a += 1) : (b += 1);
      if (a >= 1 && b >= 2) return console.log(s.join(""));
      return;
    }
    for (const v of arr) {
      if (v > s[s.length - 1]) {
        s.push(v);
        dfs(s);
        s.pop();
      }
    }
  };
  arr.sort();
  for (let i = 0; i < c - l + 1; i += 1) dfs([arr[i]]);
}

solution(4, 6, ["a", "t", "c", "i", "s", "w"]);
