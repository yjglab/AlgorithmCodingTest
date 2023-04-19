function solution(n, formula, numbers) {
  formula = formula.split("");
  const s = [];
  const table = {};
  const isAlpha = /[A-Z]/;
  formula.forEach((v) => {
    if (isAlpha.test(v) && !table[v]) table[v] = numbers.shift();
  });
  formula.forEach((v, i) => {
    if (isAlpha.test(v)) formula[i] = table[v];
  });
  for (let i = 0; i < formula.length; i += 1) {
    if (!isNaN(formula[i])) s.push(formula[i]);
    else {
      const [a, b] = [s.pop(), s.pop()];
      s.push(eval("" + b + formula[i] + a));
    }
  }
  return s[0].toFixed(2);
}
console.log(solution(5, "ABC*+DE/-", [1, 2, 3, 4, 5]));
console.log(solution(1, "AA+A+", [1]));
