function solution(relation) {
  const getCombinations = (arr, num) => {
    const combs = [];
    if (num === 1) return arr.map((v) => [v]);
    arr.forEach((fixed, index, origin) => {
      const rest = origin.slice(index + 1);
      const combinations = getCombinations(rest, num - 1);
      const attached = combinations.map((v) => [fixed, ...v]);
      combs.push(...attached);
    });
    return combs;
  };

  let result = 0;
  let table = Array.from({ length: relation[0].length }, () => []);
  relation.forEach((r) => {
    for (let ri = 0; ri < r.length; ri += 1) table[ri].push(r[ri]);
  });
  for (let ti = 0; ti < table.length; ti += 1) {
    if (table[ti].length === new Set(table[ti]).size) {
      result += 1;
      delete table[ti];
    }
  }
  table = table.filter((t) => t);
  if (table.length <= 1) return result;
  const cIdx = table.map((t, i) => i);
  const candidate = [];
  for (let i = 2; i <= table.length; i += 1) {
    const combinations = getCombinations(cIdx, i);
    for (const comb of combinations) {
      let next = false;
      for (const cand of candidate)
        if (cand.every((v) => comb.includes(v))) next = true;
      if (next) continue;

      const combCheck = [];
      for (let j = 0; j < relation.length; j += 1) {
        let combined = "";
        comb.forEach((c) => (combined += table[c][j]));
        combCheck.push(combined);
      }
      if (combCheck.length === new Set(combCheck).size) {
        result += 1;
        candidate.push(comb);
      }
    }
  }
  return result;
}
