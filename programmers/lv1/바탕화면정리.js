function solution(w) {
  let wx = w[0].length;
  let wy = w.length;
  let x, y, dx, dy;
  for (let i = 0; i < wy; i += 1) {
    if (w[i].includes("#")) {
      x = i;
      break;
    }
  }
  lp1: for (let i = 0; i < wx; i += 1) {
    for (let j = 0; j < wy; j += 1) {
      if (w[j][i] === "#") {
        y = i;
        break lp1;
      }
    }
  }
  for (let i = wy - 1; i >= 0; i -= 1) {
    if (w[i].includes("#")) {
      dx = i;
      break;
    }
  }
  lp2: for (let i = wx - 1; i >= 0; i -= 1) {
    for (let j = wy - 1; j >= 0; j -= 1) {
      if (w[j][i] === "#") {
        dy = i;
        break lp2;
      }
    }
  }

  return [x, y, dx + 1, dy + 1];
}

function solution(w) {
  let left = [];
  let top = [];
  let right = [];
  let bottom = [];
  w.forEach((v, i) => {
    [...v].forEach((val, ind) => {
      if (val === "#") {
        left.push(i);
        top.push(ind);
        right.push(i + 1);
        bottom.push(ind + 1);
      }
    });
  });
  return [
    Math.min(...left),
    Math.min(...top),
    Math.max(...right),
    Math.max(...bottom),
  ];
}
