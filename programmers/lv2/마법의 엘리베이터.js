function solution(storey) {
  let stor = "" + storey;
  let result = 0;
  for (let i = stor.length - 1; i >= 0; i -= 1) {
    const digit = 10 ** (stor.length - 1 - i);
    const diff = stor[i] >= 5 ? 10 - +stor[i] : +stor[i];
    result += diff;
    const [inc, dec] = [
      "" + (+stor + diff * digit),
      "" + (+stor - diff * digit),
    ];
    if (stor[i] == 5) {
      if (i - 1 >= 0 && stor[i - 1] >= 5) stor = inc;
      else stor = dec;
    } else if (stor[i] > 5) {
      stor = inc;
      if (stor.length > ("" + storey).length) ++i;
    } else stor = dec;
  }
  return result;
}

function solution(storey) {
  let answer = Number.MAX_SAFE_INTEGER;

  const dfs = (num, counter) => {
    if (counter >= answer) return;
    if (num === 0) {
      answer = counter;
      return;
    }

    let res = num % 10; // 4

    dfs((num - res) / 10, counter + res);
    dfs((num - res) / 10 + 1, counter + 10 - res);
  };

  dfs(storey, 0);
  return answer;
}
