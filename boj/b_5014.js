function solution(n, s, target, u, d) {
  const visited = Array(n + 1).fill(0);
  let result = 0;
  while (true) {
    if (visited[s]) return "use the stairs";
    visited[s] = 1;
    if (s === target) return result;
    else if (s < target) {
      if (s + u <= n) s += u;
      else if (s - d >= 1) s -= d;
    } else if (s > target) {
      if (s - d >= 1) s -= d;
      else if (s + u <= n) s += u;
    }
    result += 1;
  }
}
solution(100, 2, 1, 1, 0);
