// time over
function getSum(q) {
  return q.reduce((acc, curr) => acc + curr, 0);
}
function solution(q1, q2) {
  let dest = parseInt((getSum(q1) + getSum(q2)) / 2);
  let tried = 0;
  while (true) {
    let a = getSum(q1);
    let b = getSum(q2);
    if (a === dest) {
      break;
    } else if (a < b) {
      q1.push(q2.shift());
      tried += 1;
    } else if (a > b) {
      q2.push(q1.shift());
      tried += 1;
    }
    if (tried === q1.length * 2) return -1;
  }
  return tried;
}

// success
function solution(q1, q2) {
  let q1s = q1.reduce((acc, curr) => acc + curr, 0);
  let q2s = q2.reduce((acc, curr) => acc + curr, 0);
  let limit = q1.length * 3;
  let dest = parseInt((q1s + q2s) / 2);
  let d1 = 0;
  let d2 = 0;
  let tried = 0;
  while (tried !== limit && q1s !== dest) {
    if (q1s < q2s) {
      q1.push(q2[d2]);
      q1s += q2[d2];
      q2s -= q2[d2++];
    } else if (q1s > q2s) {
      q2.push(q1[d1]);
      q2s += q1[d1];
      q1s -= q1[d1++];
    }
    tried += 1;
  }
  return tried === limit ? -1 : tried;
}
