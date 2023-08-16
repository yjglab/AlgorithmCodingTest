function solution(targets) {
  let result = 1;
  let now = [0, 100_000_000];
  const scoped = (now, target) =>
    now[1] > target[0]
      ? [Math.max(now[0], target[0]), Math.min(now[1], target[1])]
      : false;
  targets.sort((a, b) => a[0] - b[0]);
  targets.forEach((target) => {
    now = scoped(now, target);
    if (!now) {
      now = target;
      result += 1;
    }
  });
  return result;
}

function solution(targets) {
  let answer = 0;
  const tgts = targets.slice().sort((a, b) => a[0] - b[0] || b[1] - a[1]);
  let tail = -1;
  tgts.forEach(([s, e]) => {
    if (tail <= s) {
      answer++;
      tail = e;
    } else if (e < tail) {
      tail = e;
    }
  });
  return answer;
}
