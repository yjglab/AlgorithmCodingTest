function solution(p) {
  if (!p) return "";
  let [u, v] = ["", ""];
  let [a, b] = [0, 0];
  for (let i = 0; i < p.length; i += 1) {
    p[i] === `(` ? ++a : ++b;
    u += p[i];
    if (a === b) {
      v = p.slice(i + 1, p.length);
      break;
    }
  }
  if (u[u.length - 1] === `)`) return u + solution(v);
  else {
    u = u.slice(1, u.length - 1).split("");
    for (let i = 0; i < u.length; i += 1) u[i] = u[i] === `)` ? `(` : `)`;
    return "(" + solution(v) + ")" + u.join("");
  }
}

//
function reverse(str) {
  return str
    .slice(1, str.length - 1)
    .split("")
    .map((c) => (c === "(" ? ")" : "("))
    .join("");
}

function solution(p) {
  if (p.length < 1) return "";

  let balance = 0;
  let pivot = 0;
  do {
    balance += p[pivot++] === "(" ? 1 : -1;
  } while (balance !== 0);

  const u = p.slice(0, pivot);
  const v = solution(p.slice(pivot, p.length));

  if (u[0] === "(" && u[u.length - 1] == ")") return u + v;
  else return "(" + v + ")" + reverse(u);
}
