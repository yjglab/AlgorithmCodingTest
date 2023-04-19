function solution(n, numbers) {
  const result = Array(n).fill(-1);
  const s = [];
  const cTable = Array(Math.max(...numbers) + 1).fill(0);

  numbers.forEach((number, i) => (cTable[number] += 1));
  numbers.forEach((number, i) => {
    while (s.length && cTable[numbers[s[s.length - 1]]] < cTable[number]) {
      result[s.pop()] = number;
    }
    s.push(i);
  });
  return result;
}
console.log(solution(3, [1000000, 2, 2]));
console.log(solution(7, [1, 1, 2, 3, 4, 2, 1]));
