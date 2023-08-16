function solution(init, operations) {
  const [ls, rs] = [init.split(""), []];
  operations.forEach((oper) => {
    oper = oper.split(" ");
    let op = oper[0];
    if (op === "L" && ls.length) rs.push(ls.pop());
    else if (op === "D" && rs.length) ls.push(rs.pop());
    else if (op === "B" && ls.length) ls.pop();
    else if (op === "P") ls.push(oper[1]);
  });
  return ls.join("") + rs.reverse().join("");
}
console.log(solution("abcd", ["P x", "L", "P y"]));
