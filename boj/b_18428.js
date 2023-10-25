function solution(n, arr) {
  const direction = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];
  let [t, result] = [0, "NO"];
  for (const i of arr) t += i.reduce((a, c) => a + (c === "T"), 0);
  const setting = (o) => {
    const finded = (r, c) => {
      for (const [p, q] of direction) {
        let [dr, dc] = [r + p, c + q];
        while (1) {
          if (dr < 0 || dc < 0 || dr >= n || dc >= n || arr[dr][dc] === "O")
            break;
          if (arr[dr][dc] === "S") return 1;
          [dr, dc] = [dr + p, dc + q];
        }
      }
    };
    if (o === 3) {
      let checked = 0;
      for (let i = 0; i < n; i += 1) {
        for (let j = 0; j < n; j += 1) {
          if (arr[i][j] === "T" && !finded(i, j)) checked += 1;
        }
      }
      if (checked === t) result = "YES";
      return;
    }
    for (let i = 0; i < n; i += 1) {
      for (let j = 0; j < n; j += 1) {
        if (arr[i][j] === "X") {
          arr[i][j] = "O";
          setting(o + 1);
          arr[i][j] = "X";
        }
      }
    }
  };

  setting(0);
  return result;
}

console.log(
  solution(5, [
    ["X", "S", "X", "X", "T"],
    ["T", "X", "S", "X", "X"],
    ["X", "X", "X", "X", "X"],
    ["X", "T", "X", "X", "X"],
    ["X", "X", "T", "X", "X"],
  ])
);
console.log(
  solution(4, [
    ["S", "S", "S", "T"],
    ["X", "X", "X", "X"],
    ["X", "X", "X", "X"],
    ["T", "T", "T", "X"],
  ])
);
