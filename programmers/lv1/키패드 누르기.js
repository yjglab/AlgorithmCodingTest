function solution(numbers, hand) {
  const l = [1, 4, 7, -3]; // * -> -3
  const m = [2, 5, 8, -2]; // 0 -> -2
  const r = [3, 6, 9, -1]; // # -> -1

  let lh = -3; // *
  let rh = -1; // #
  let result = "";

  for (let v of numbers) {
    if (v === 0) v = -2;
    if (l.includes(v)) {
      // 1,4,7인 경우
      result += "L";
      lh = v;
    } else if (r.includes(v)) {
      // 3,6,9인 경우
      result += "R";
      rh = v;
    } else {
      // 2,5,8,-2인 경우
      let lDist = 0;
      let rDist = 0;

      if (l.includes(lh)) {
        // 왼쪽손이 좌측인 경우
        lDist = Math.abs(m.indexOf(lh + 1) - m.indexOf(v)) + 1; // 가운데로 이동 후 목표와의 거리 계산
      } else {
        // 왼쪽손이 중앙인 경우
        lDist = Math.abs(m.indexOf(lh) - m.indexOf(v)); // 현재 위치에서 목표와의 거리 계산
      }
      if (r.includes(rh)) {
        // 오른쪽손이 우측인 경우
        rDist = Math.abs(m.indexOf(rh - 1) - m.indexOf(v)) + 1; // 가운데로 이동 후 목표와의 거리 계산
      } else {
        // 오른쪽손이 중앙인 경우
        rDist = Math.abs(m.indexOf(rh) - m.indexOf(v)); // 현재 위치에서 목표와의 거리 계산
      }
      if (lDist === rDist) {
        // 거리가 동일한 경우
        const h = hand === "left" ? "L" : "R";
        result += h;
        if (h === "L") lh = v;
        else if (h === "R") rh = v;
      } else {
        // 거리가 다른 경우
        if (lDist < rDist) {
          result += "L";
          lh = v;
        } else if (lDist > rDist) {
          result += "R";
          rh = v;
        }
      }
    }
  }
  return result;
}
