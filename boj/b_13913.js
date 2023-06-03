function solution(n, k) {
  let ptr = -1;
  const q = [[n, 0, [n]]];
  const arr = Array(200001).fill(0);
  let resultCnt = 0;
  let resultPassed = [];
  while (true) {
    const [now, cnt, passed] = q[++ptr];
    if (n > k) {
      resultCnt = n - k;
      for (let i = n; i >= k; i -= 1) {
        resultPassed.push(i);
      }
      break;
    }
    if (now === k) {
      resultCnt = cnt;
      resultPassed = passed;
      break;
    }
    for (const i of [now - 1, now + 1, now * 2]) {
      if (i < 0 || i > 100000) continue;
      if (!arr[i]) {
        arr[i] = 1;
        q.push([i, cnt + 1, passed.concat(i)]);
      }
    }
  }
  return [resultCnt, resultPassed];
}
console.log(solution(5, 17));
