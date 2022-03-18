let arr = prompt()
  .split("")
  .map((v) => parseInt(v));

function solution(arr) {
  if (arr.length == 1) return arr[0];
  let result = Math.max(arr[0] + arr[1], arr[0] * arr[1]);
  for (let i = 2; i < arr.length; i += 1) {
    if (result + arr[i] < result * arr[i]) {
      result *= arr[i];
    } else {
      result += arr[i];
    }
  }
  return result;
}
