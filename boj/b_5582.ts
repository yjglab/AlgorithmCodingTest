function sol5582(s1: string, s2: string) {
  const d = Array.from({ length: s1.length + 1 }, () =>
    Array(s2.length + 1).fill(0)
  );
  let result = 0;
  for (let i = 1; i <= s1.length; i += 1) {
    for (let j = 1; j <= s2.length; j += 1) {
      if (s1[i - 1] === s2[j - 1]) {
        d[i][j] = d[i - 1][j - 1] + 1;
        result = Math.max(result, d[i][j]);
      }
    }
  }
  return result;
}

console.log(sol5582("ABRACADABRA", "ECADADABRBCRDARA"));
