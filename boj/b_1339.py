import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
cands, num = [0] * 26, 9
for _ in range(n):
    cand = list(input().rstrip())
    for i in range(len(cand)):
        cands[ord(cand[i]) - 65] += 10 ** (len(cand) - i - 1)
cands.sort(reverse=True)
for i in range(10):
    if not cands[i]:
        break
    cands[i] *= num
    num -= 1
print(sum(cands))