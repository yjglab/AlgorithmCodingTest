function solution(arr) {
  const result = [];
  arr.forEach((str) => {
    let s = str.split(" ");
    s = s.map((v) => v.split("").reverse().join(""));
    result.push(s.join(" "));
  });
  console.log(result);
}
solution(["I am happy today", "We want to win the first prize"]);
