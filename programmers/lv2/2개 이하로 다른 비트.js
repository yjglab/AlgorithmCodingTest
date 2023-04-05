function solution(numbers) {
  const result = [];
  numbers.forEach((v) => {
    if (v % 2 === 0) result.push(v + 1);
    else {
      let bin = v.toString(2);
      let m = "1" + "0".repeat(bin.length - bin.lastIndexOf("0") - 1);
      result.push(v + parseInt(m, 2) - parseInt(parseInt(m, 2) / 2));
    }
  });
  return result;
}
