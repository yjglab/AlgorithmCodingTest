function sol2470(n: number, arr: Array<number>) {
  arr.sort((a, b) => a - b);
  let [l, r, accr] = [0, n - 1, Number.MAX_SAFE_INTEGER];
  let result;
  while (l != r) {
    const now = arr[l] + arr[r];
    const p = Math.abs(now);
    if (p < accr) {
      accr = p;
      result = [arr[l], arr[r]];
    }
    if (now > 0) r -= 1;
    else if (now < 0) l += 1;
    else break;
  }
  console.log(result);
}

sol2470(5, [-2, 4, -99, -1, 98]);
