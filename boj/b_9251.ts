function sol9251(a: string, b: string) {
  const d: number[][] = Array.from({ length: a.length + 1 }, () =>
    Array(b.length + 1).fill(0)
  );
  for (let i = 0; i < a.length; i += 1) {
    for (let j = 0; j < b.length; j += 1) {
      if (a[i] === b[j]) d[i + 1][j + 1] = d[i][j] + 1;
      else d[i + 1][j + 1] = Math.max(d[i + 1][j], d[i][j + 1]);
    }
  }
  console.log(d[a.length][b.length]);
}
sol9251("ACAYKP", "CAPCAK");
