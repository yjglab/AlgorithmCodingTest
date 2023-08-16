function sol2217(n: number, arr: Array<number>) {
  arr.sort((a, b) => b - a);
  const result = [];
  for (let i = 0; i < n; i += 1) result.push(arr[i] * (i + 1));
  console.log(Math.max(...result));
}
sol2217(2, [10, 15]);
