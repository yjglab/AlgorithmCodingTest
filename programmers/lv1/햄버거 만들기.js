function solution(ingredient) {
  let cnt = 0;
  for (let i = 3; i < ingredient.length; i += 1) {
    const now = ingredient[i];
    if (
      now === 1 &&
      ingredient[i - 1] === 3 &&
      ingredient[i - 2] === 2 &&
      ingredient[i - 3] === 1
    ) {
      ingredient.splice(i - 3, 4);
      cnt += 1;
      i -= 4;
    }
  }
  return cnt;
}

// 타임아웃
function solution(ingredient) {
  let cnt = 0;
  ingredient = ingredient.join("");
  while (true) {
    if (ingredient.includes("1231")) {
      ingredient = ingredient.replace("1231", "");
      cnt += 1;
    } else return cnt;
  }
}
