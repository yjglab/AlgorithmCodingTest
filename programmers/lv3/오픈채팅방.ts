function 오픈채팅방(records: string[]) {
  let result = [];
  const users: { [key: string]: string } = {};
  for (const record of records) {
    const r = record.split(" ");
    const opt = r[0];
    if (opt === "Enter") {
      const [id, name] = [r[1], r[2]];
      users[id] = name;
      result.push(`${id}님이 들어왔습니다.`);
    } else if (opt === "Leave") {
      const id = r[1];
      result.push(`${id}님이 나갔습니다.`);
    } else {
      const [id, name] = [r[1], r[2]];
      users[id] = name;
    }
  }
  return result.map((v) => {
    const id = v.slice(0, v.indexOf("님"));
    return v.replace(id, users[id]);
  });
}
