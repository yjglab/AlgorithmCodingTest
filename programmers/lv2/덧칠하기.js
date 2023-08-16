function solution(n, m, section) {
  let result = 0;
  const arr = Array(n).fill(1);
  for (const s of section) {
    arr[s - 1] = 0;
  }
  for (const s of section) {
    if (!arr[s - 1]) {
      for (let i = s - 1; i < s + m - 1; i += 1) {
        arr[i] = 1;
      }
      result += 1;
    }
    if (!arr.includes(0)) {
      return result;
    }
  }
}
