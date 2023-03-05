// kakao 2021 blind recruitment

function solution(id) {
  id = id.toLowerCase().split("");

  const ptn = /^[a-z0-9\_\-\.]*$/;
  let ids = [];
  for (let i of id) {
    if (ptn.test(i)) ids.push(i);
  }
  for (let i = 1; i < ids.length; i += 1) {
    if (ids[i] === "." && ids[i - 1] === ".") {
      ids.splice(i, 1);
      i -= 1;
    }
  }
  if (ids[0] === ".") ids.shift();
  if (ids[ids.length - 1] === ".") ids.pop();
  if (!ids.length) ids.push("a");

  if (ids.length >= 16) ids = ids.splice(0, 15);
  if (ids[ids.length - 1] === ".") ids.pop();
  ids = ids.join("");
  while (true) {
    if (ids.length > 2) break;
    else ids = ids.concat(ids[ids.length - 1]);
  }

  return ids;
}

function solution(new_id) {
  const answer = new_id
    .toLowerCase() // 1
    .replace(/[^\w-_.]/g, "") // 2
    .replace(/\.+/g, ".") // 3
    .replace(/^\.|\.$/g, "") // 4
    .replace(/^$/, "a") // 5
    .slice(0, 15)
    .replace(/\.$/, ""); // 6
  const len = answer.length;
  return len > 2 ? answer : answer + answer.charAt(len - 1).repeat(3 - len);
}
