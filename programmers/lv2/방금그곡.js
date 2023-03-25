function solution(m, musicinfos) {
  const replaceSharp = (str) =>
    str
      .replaceAll("A#", "a")
      .replaceAll("G#", "g")
      .replaceAll("F#", "f")
      .replaceAll("D#", "d")
      .replaceAll("C#", "c");
  const result = [];
  m = replaceSharp(m);
  for (const musicinfo of musicinfos) {
    let [stime, etime, title, info] = musicinfo.split(",");
    info = replaceSharp(info);
    stime = stime.split(":");
    etime = etime.split(":");
    let time = (etime[0] - stime[0]) * 60 + (etime[1] - stime[1]);
    let cnt = 0;
    let fulloutput = "";
    while (cnt < time) {
      fulloutput += info[cnt % info.length];
      cnt += 1;
    }
    if (fulloutput.includes(m)) result.push([title, time]);
  }
  if (result.length) {
    let [rname, rtime] = result.sort((a, b) => a[1] - b[1])[result.length - 1];
    let rcnt = 0;
    result.forEach((v) => {
      if (v[1] === rtime) rcnt += 1;
    });
    if (rcnt > 1) return result.find((v) => v[1] === rtime)[0];
    else return rname;
  } else {
    return "(None)";
  }
}
