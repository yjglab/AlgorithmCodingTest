function solution(n) {
  if (n === 1) return [1];
  if (n === 2) return [1, 2, 3];
  const arr = Array(n).fill();
  for (let i = 0; i < n; i += 1) {
    arr[i] = Array(i + 1).fill(-1);
  }
  let idx = 1;
  let [cx, cy] = [-1, 0];

  while (1) {
    if (
      arr[cx + 1][cy] !== -1 &&
      arr[cx][cy + 1] !== -1 &&
      arr[cx - 1][cy - 1] !== -1
    )
      break;
    while (cx + 1 < n && arr[cx + 1][cy] === -1) {
      cx += 1;
      arr[cx][cy] = idx++;
    }
    while (cy + 1 < n && arr[cx][cy + 1] === -1) {
      cy += 1;
      arr[cx][cy] = idx++;
    }
    while (cx - 1 >= 0 && arr[cx - 1][cy - 1] === -1) {
      cx -= 1;
      cy -= 1;
      arr[cx][cy] = idx++;
    }
  }
  return arr.flat();
}
