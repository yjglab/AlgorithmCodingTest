function solution(n, l, r, arr) {
  let result = 0;
  const dir = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];
  const transfer = (sr, sc, visited) => {
    const q = [[sr, sc]];
    let front = 0;
    const targets = [[sr, sc]];
    let targetsSum = arr[sr][sc];

    while (q[front]) {
      const [qr, qc] = q[front++];
      for (const [x, y] of dir) {
        const [dr, dc] = [qr + x, qc + y];
        if (dr < 0 || dc < 0 || dr >= n || dc >= n) continue;
        if (visited[dr][dc]) continue;

        const diff = Math.abs(arr[qr][qc] - arr[dr][dc]);
        if (diff >= l && diff <= r) {
          visited[dr][dc] = 1;
          targets.push([dr, dc]);
          targetsSum += arr[dr][dc];
          q.push([dr, dc]);
        }
      }
    }
    return [targets, targetsSum];
  };
  while (1) {
    const visited = Array.from({ length: n }, () => Array(n).fill(0));
    const candidates = [];
    for (let i = 0; i < n; i += 1) {
      for (let j = 0; j < n; j += 1) {
        if (!visited[i][j]) {
          visited[i][j] = 1;
          const [targets, targetsSum] = transfer(i, j, visited);
          if (targets.length > 1) candidates.push([targets, targetsSum]);
        }
      }
    }
    if (!candidates[0]) return result;
    for (const [targets, targetsSum] of candidates) {
      const size = parseInt(targetsSum / targets.length);
      for (const [tr, tc] of targets) arr[tr][tc] = size;
    }
    result += 1;
  }
}
console.log(
  solution(3, 5, 10, [
    [10, 15, 20],
    [20, 30, 25],
    [40, 22, 10],
  ])
);
