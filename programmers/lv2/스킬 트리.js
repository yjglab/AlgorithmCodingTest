function solution(skill, skill_trees) {
  const table = {};
  skill.split("").forEach((s, i) => (table[s] = i));
  let result = 0;
  for (const st of skill_trees) {
    const order = Array(skill.length).fill(0);
    let avail = true;
    for (let i = 0; i < st.length; i += 1) {
      if (!skill.includes(st[i])) continue;
      for (let j = 0; j < table[st[i]]; j += 1) {
        if (!order[j]) avail = false;
      }
      if (avail) order[table[st[i]]] = 1;
    }
    if (avail) result += 1;
  }
  return result;
}

function solution(skill, skill_trees) {
  var answer = 0;
  var regex = new RegExp(`[^${skill}]`, "g");

  return skill_trees
    .map((x) => x.replace(regex, ""))
    .filter((x) => {
      return skill.indexOf(x) === 0 || x === "";
    }).length;
}
