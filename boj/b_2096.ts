function sol2096(n: number, arr: Array<Array<number>>) {
  let [mx1, mx2, mx3] = arr[0];
  let [mn1, mn2, mn3] = arr[0];
  for (let i = 1; i < n; i += 1) {
    const [a, b, c] = arr[i];
    const [pmx1, pmx2, pmx3, pmn1, pmn2, pmn3] = [mx1, mx2, mx3, mn1, mn2, mn3];
    mx1 = a + Math.max(pmx1, pmx2);
    mx2 = b + Math.max(pmx1, pmx2, pmx3);
    mx3 = c + Math.max(pmx2, pmx3);
    mn1 = a + Math.min(pmn1, pmn2);
    mn2 = b + Math.min(pmn1, pmn2, pmn3);
    mn3 = c + Math.min(pmn2, pmn3);
  }
  return [Math.max(mx1, mx2, mx3), Math.min(mn1, mn2, mn3)];
}
console.log(
  sol2096(3, [
    [1, 2, 3],
    [4, 5, 6],
    [4, 9, 0],
  ])
);
