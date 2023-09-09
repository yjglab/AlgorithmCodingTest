function solution(str1, str2) {
  [str1, str2] = [str1.toLowerCase(), str2.toLowerCase()];
  const isAlpha = (v) => {
    if (v.charCodeAt() >= 97 && v.charCodeAt() <= 122) return true;
    return false;
  };
  const [s1, s2] = [{}, {}];
  const divide = (arr, chart) => {
    for (let i = 1; i < arr.length; i += 1) {
      const [a, b] = [arr[i - 1], arr[i]];
      if (isAlpha(a) && isAlpha(b)) {
        if (chart[a + b]) chart[a + b] += 1;
        else chart[a + b] = 1;
      }
    }
  };
  divide(str1, s1), divide(str2, s2);
  let [inter, union] = [0, 0];
  for (const key of Object.keys(s1)) {
    if (s2[key]) {
      inter += Math.min(s1[key], s2[key]);
      union += Math.max(s1[key], s2[key]);
    } else {
      union += s1[key];
    }
  }
  for (const key of Object.keys(s2)) {
    if (!s1[key]) union += s2[key];
  }
  if (union === 0) return 65536;
  return Math.floor((inter / union) * 65536);
}
