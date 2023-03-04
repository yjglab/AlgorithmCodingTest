function solution(cards1, cards2, goal) {
  for (let g of goal) {
    if (!cards1.indexOf(g)) {
      cards1.shift();
    } else if (!cards2.indexOf(g)) {
      cards2.shift();
    } else {
      return "No";
    }
  }
  return "Yes";
}
