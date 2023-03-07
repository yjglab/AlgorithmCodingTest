function solution(s, skip, index) {
  let answer = "";
  for (let apt of s) {
    let aptCode = apt.charCodeAt();
    let i = index;

    while (i > 0) {
      aptCode = aptCode === 122 ? 97 : aptCode + 1;
      if (!skip.includes(String.fromCharCode(aptCode))) {
        i -= 1;
      }
    }
    answer += String.fromCharCode(aptCode);
  }
  return answer;
}

function solution(s, skip, index) {
  const alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
  ].filter((c) => !skip.includes(c));
  return s
    .split("")
    .map((c) => alphabet[(alphabet.indexOf(c) + index) % alphabet.length])
    .join("");
}
