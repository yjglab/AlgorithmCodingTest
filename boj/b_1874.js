function solution(arr) {
  let [result, s, a] = [[], [], 1];
  arr.forEach((v) => {
    if (s.length && s[s.length - 1] == v) {
      s.pop();
      result.push("-");
    } else {
      for (let i = a; i <= v; i += 1) {
        s.push(i);
        result.push("+");
      }
      s.pop();
      result.push("-");
      a = v + 1;
    }
  });
  if (!s.length) return result;
  else return "NO";
}
console.log(solution([4, 3, 6, 8, 7, 5, 2, 1]));
