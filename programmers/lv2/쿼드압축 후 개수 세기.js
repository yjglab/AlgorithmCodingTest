let [zero, one] = [0, 0];
function solution(arr) {
  let arrFlat = arr.flat();
  if (!arrFlat.includes(0)) return [0, 1];
  else if (!arrFlat.includes(1)) return [1, 0];

  if (arrFlat.length === 1) {
    if (arrFlat[0] === 0) return (zero += 1);
    else if (arrFlat[0] === 1) return (one += 1);
  }
  let end = arr.length;
  let mid = parseInt(end / 2);
  let [lt, rt, lb, rb] = Array.from({ length: 4 }, () => []);

  arr.slice(0, mid).forEach((v) => lt.push(v.slice(0, mid)));
  arr.slice(0, mid).forEach((v) => rt.push(v.slice(mid, end)));
  arr.slice(mid, end).forEach((v) => lb.push(v.slice(0, mid)));
  arr.slice(mid, end).forEach((v) => rb.push(v.slice(mid, end)));

  for (const a of [lt, rt, lb, rb]) {
    if (!a.flat().includes(0)) one += 1;
    else if (!a.flat().includes(1)) zero += 1;
    else solution(a);
  }
  return [zero, one];
}

function solution(arr) {
  const quadZip = (row, col, n) => {
    if (n < 2) return arr[row][col] ? [0, 1] : [1, 0];
    let cnt0 = 0,
      cnt1 = 0;
    n >>= 1;
    for (let [i, j] of [
      [0, 0],
      [0, 1],
      [1, 0],
      [1, 1],
    ]) {
      let [zero, one] = quadZip(row + i * n, col + j * n, n);
      cnt0 += zero;
      cnt1 += one;
    }
    if (cnt0 === 0) return [0, 1];
    if (cnt1 === 0) return [1, 0];
    return [cnt0, cnt1];
  };
  return quadZip(0, 0, arr.length);
}
