function solution(prs, location) {
  let now = 0;
  prs[location] = prs[location].toString();
  while (prs.length) {
    const p = prs.shift();
    if (p < Math.max(...prs)) prs.push(p);
    else {
      if (typeof p === "string") return ++now;
      ++now;
    }
  }
}
