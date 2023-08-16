function solution(today, terms, privacies) {
  const term = {};
  terms.forEach((v) => {
    const [a, b] = v.split(" ");
    term[a] = parseInt(b);
  });
  let answer = [];
  privacies.forEach((p, idx) => {
    let y, m, d;
    let [date, tm] = p.split(" ");
    let [pYear, pMonth, pDay] = date.split(".").map((v) => parseInt(v));
    y = pYear + parseInt((pMonth + term[tm]) / 12);
    m = (pMonth + term[tm]) % 12;
    d = pDay - 1;
    if (m === 0) {
      y -= 1;
      m = 12;
    }
    if (d === 0) {
      m -= 1;
      d = 28;
    }
    let result = parseInt(
      y + `${m < 10 ? "0" + m : m}` + `${d < 10 ? "0" + d : d}`
    );
    if (result < parseInt(today.replaceAll(".", ""))) answer.push(idx + 1);
  });
  return answer;
}

function solution(today, terms, privacies) {
  var answer = [];
  var [year, month, date] = today.split(".").map(Number);
  var todates = year * 12 * 28 + month * 28 + date;
  var t = {};
  terms.forEach((e) => {
    let [a, b] = e.split(" ");
    t[a] = Number(b);
  });
  privacies.forEach((e, i) => {
    var [day, term] = e.split(" ");
    day = day.split(".").map(Number);
    var dates = day[0] * 12 * 28 + day[1] * 28 + day[2] + t[term] * 28;
    if (dates <= todates) answer.push(i + 1);
  });
  return answer;
}
