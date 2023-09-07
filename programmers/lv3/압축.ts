function sol압축(msg: string) {
  const chart: { [key: string]: number } = {};
  let r = [];
  for (let i = 65; i <= 90; i += 1) {
    chart[String.fromCharCode(i)] = i - 64;
  }
  let [n, now] = [27, ""];
  for (let i = 0; i < msg.length; i += 1) {
    now += msg[i];
    if (chart[now]) continue;
    else {
      chart[now] = n++;
      r.push(chart[now.slice(0, now.length - 1)]);
      now = "";
      i -= 1;
    }
  }
  r.push(chart[now]);
  return r;
}
