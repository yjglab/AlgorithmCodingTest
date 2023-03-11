function solution(word) {
  let aptSet = { A: 0, E: 1, I: 2, O: 3, U: 4 };
  let result = 0;
  let i = 4;
  for (const w of word) {
    let wi = i;
    let mid = 0;
    while (wi > -1) {
      mid += 5 ** wi;
      wi -= 1;
    }
    result += mid * aptSet[w] + 1;
    i -= 1;
  }
  return result;
}

function solution(words) {
  return words
    .split("")
    .reduce(
      (r, c, i) =>
        r + [781, 156, 31, 6, 1][i] * ["A", "E", "I", "O", "U"].indexOf(c) + 1,
      0
    );
}
