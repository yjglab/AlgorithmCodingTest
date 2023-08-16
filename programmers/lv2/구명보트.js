function solution(people, limit) {
  people = people.sort((a, b) => a - b);
  let result = 0;
  let [s, e] = [0, people.length - 1];
  while (s <= e) {
    let curr = people[s] + people[e];
    if (curr <= limit) s += 1;
    e -= 1;
    result += 1;
  }

  return result;
}
