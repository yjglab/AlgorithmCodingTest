function solution(n, str) {
  const cands = Array(26).fill(0);
  let num = 9;
  str.forEach((cand) => {
    for (let i = 0; i < cand.length; i += 1) {
      cands[cand[i].charCodeAt() - 65] += 10 ** (cand.length - i - 1);
    }
  });
  cands.sort((a, b) => b - a);
  for (let i = 0; i < 10; i += 1) {
    if (!cands[i]) break;
    cands[i] *= num--;
  }
  return cands.reduce((accr, curr) => accr + curr, 0);
}
solution(2, ["GCF", "ACDEB"]);
