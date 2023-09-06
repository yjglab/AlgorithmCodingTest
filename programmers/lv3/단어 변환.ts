function 단어변환(begin: string, target: string, words: Array<string>) {
  const visited = Array(words.length).fill(0);

  let result = 50;
  const dfs = (now: string, cnt: number) => {
    if (now === target) return (result = Math.min(result, cnt));

    for (let i = 0; i < now.length; i += 1) {
      const [l, r] = [now.slice(0, i), now.slice(i + 1, now.length)];
      for (let j = 0; j < words.length; j += 1) {
        const [wl, wr] = [
          words[j].slice(0, i),
          words[j].slice(i + 1, words[j].length),
        ];
        if (l + r === wl + wr && !visited[j]) {
          visited[j] = 1;
          dfs(words[j], cnt + 1);
          visited[j] = 0;
        }
      }
    }
  };
  dfs(begin, 0);
  if (result === 50) return 0;
  return result;
}
console.log(단어변환("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]));
