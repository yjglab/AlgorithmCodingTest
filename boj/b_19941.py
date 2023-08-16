import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, k = map(int, input().split())
s = input().rstrip()
vst = [1] * n
for i in range(n):
    if s[i] == "H":
        vst[i] = 0
result = 0
for i in range(n):
    if s[i] == "P":
        checked = 0
        for l in range(i - k, i):
            if l < 0:
                continue
            if s[l] == "H" and not vst[l]:
                result += 1
                vst[l] = 1
                checked = 1
                break
        if checked:
            continue
        for r in range(i + 1, i + 1 + k):
            if r >= n:
                break
            if s[r] == "H" and not vst[r]:
                result += 1
                vst[r] = 1
                break
print(result)


