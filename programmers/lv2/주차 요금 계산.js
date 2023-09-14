function solution(fees, records) {
  const [baseTime, baseFee, unitTime, unitFee] = fees;
  const charts = {};
  for (const record of records) {
    const [time, number, status] = record.split(" ");
    const [h, m] = time.split(":").map((v) => parseInt(v));
    if (status === "IN") {
      if (!charts[number] || !charts[number][1])
        charts[number] = [[h, m], 0, status];
      else {
        charts[number][0] = [h, m];
        charts[number][2] = status;
      }
    } else if (status === "OUT") {
      const [ph, pm] = charts[number][0];
      charts[number][1] += (h - ph) * 60 + (m - pm);
      charts[number][2] = status;
    }
  }
  for (const chart of Object.entries(charts)) {
    if (chart[1][2] === "IN") {
      const [ph, pm] = chart[1][0];
      charts[chart[0]][1] += (23 - ph) * 60 + (59 - pm);
    }
  }
  const result = [];
  Object.entries(charts)
    .sort((a, b) => parseInt(a[0]) - parseInt(b[0]))
    .forEach((v) => {
      const time = v[1][1];
      if (time <= baseTime) result.push(baseFee);
      else
        result.push(
          baseFee + Math.ceil((time - baseTime) / unitTime) * unitFee
        );
    });
  return result;
}
