function order(i) {
  if (i === 6) return 1;
  else if (i === 5) return 2;
  else if (i === 4) return 3;
  else if (i === 3) return 4;
  else if (i === 2) return 5;
  else return 6;
}
function solution(lottos, win_nums) {
  let mx = 0;
  let mn = 0;
  lottos.forEach((v) => {
    if (win_nums.includes(v)) mn += 1;
  });
  lottos.forEach((v) => {
    if (v === 0) mx += 1;
  });
  return [order(mx + mn), order(mn)];
}

function solution(lottos, win_nums) {
  const rank = [6, 6, 5, 4, 3, 2, 1];

  let minCount = lottos.filter((v) => win_nums.includes(v)).length;
  let zeroCount = lottos.filter((v) => !v).length;

  const maxCount = minCount + zeroCount;

  return [rank[maxCount], rank[minCount]];
}
