function solution(n) {
  let result = "";
  while (n) {
    if (n % 3 !== 0) {
      result = (n % 3) + result;
      n = parseInt(n / 3);
    } else {
      result = 3 + result;
      n = parseInt(n / 3) - 1;
    }
  }
  return result.replaceAll("3", "4");
}

function change124(n) {
  return n === 0
    ? ""
    : change124(parseInt((n - 1) / 3)) + [1, 2, 4][(n - 1) % 3];
}
