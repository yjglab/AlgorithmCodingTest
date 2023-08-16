function solution(n, m, array) {
  const deq = [];
  for (let i = 0; i < n; i += 1) {
    for (let j = 0; j < m; j += 1) {
      if (array[i][j] === 2) deq.push([i, j]);
    }
  }
  const bfs = () => {
    const q = deq.slice();
    let front = 0;
    const arr = JSON.parse(JSON.stringify(array));
    while (q[front]) {
      const [r, c] = q[front++];
      for (const d of [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1],
      ]) {
        const [dr, dc] = [r + d[0], c + d[1]];
        if (dr < 0 || dc < 0 || dr >= n || dc >= m) continue;
        if (!arr[dr][dc]) {
          arr[dr][dc] = 2;
          q.push([dr, dc]);
        }
      }
    }
    let res = 0;
    for (let i = 0; i < n; i += 1) {
      for (let j = 0; j < m; j += 1) {
        if (!arr[i][j]) res += 1;
      }
    }
    return res;
  };
  let result = 0;
  const setWall = (cnt) => {
    if (cnt == 3) return (result = Math.max(result, bfs()));
    for (let i = 0; i < n; i += 1) {
      for (let j = 0; j < m; j += 1) {
        if (!array[i][j]) {
          array[i][j] = 1;
          setWall(cnt + 1);
          array[i][j] = 0;
        }
      }
    }
  };
  setWall(0);
  return result;
}
console.log(
  solution(7, 7, [
    [2, 0, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 2, 0],
    [0, 1, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
  ])
);
