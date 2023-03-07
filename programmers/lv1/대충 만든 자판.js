function solution(keymap, targets) {
  const answer = [];
  for (const target of targets) {
    let sumOfMin = 0;
    for (let i = 0; i < target.length; i += 1) {
      const table = Array(keymap.length).fill();
      for (let j = 0; j < keymap.length; j += 1) {
        if (keymap[j].includes(target[i]))
          table[j] = keymap[j].indexOf(target[i]);
        else table[j] = Number.MAX_VALUE;
      }
      sumOfMin += Math.min(...table) + 1;
    }
    if (sumOfMin < Number.MAX_VALUE) answer.push(sumOfMin);
    else answer.push(-1);
  }
  return answer;
}

function solution(keymap, targets) {
  const answer = [];
  const map = {};
  for (const items of keymap) {
    items
      .split("")
      .map(
        (item, index) =>
          (map[item] = map[item] < index + 1 ? map[item] : index + 1)
      );
  }
  for (const items of targets) {
    answer.push(
      items.split("").reduce((cur, item) => (cur += map[item]), 0) || -1
    );
  }
  return answer;
}
