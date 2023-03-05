function solution(id_list, report, k) {
  const reportTable = Array.from({ length: id_list.length }, () => []);
  const answer = Array(id_list.length).fill(0);

  report.forEach((v) => {
    const [reporter, reported] = v.split(" ");
    const reportedIdx = id_list.indexOf(reported);
    if (!reportTable[reportedIdx].includes(reporter)) {
      reportTable[reportedIdx].push(reporter);
    }
  });
  reportTable.forEach((v) => {
    if (v.length >= k) {
      v.forEach((e) => (answer[id_list.indexOf(e)] += 1));
    }
  });
  return answer;
}

function solution(id_list, report, k) {
  let reports = [...new Set(report)].map((a) => {
    return a.split(" ");
  });
  let counts = new Map();
  for (const bad of reports) {
    counts.set(bad[1], counts.get(bad[1]) + 1 || 1);
  }
  let good = new Map();
  for (const report of reports) {
    if (counts.get(report[1]) >= k) {
      good.set(report[0], good.get(report[0]) + 1 || 1);
    }
  }
  let answer = id_list.map((a) => good.get(a) || 0);
  return answer;
}
