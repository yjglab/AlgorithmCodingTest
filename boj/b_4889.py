import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = 0
while 1:
    n += 1
    t = input().strip()
    if t[0] == "-":
        break
    result = 0
    s = []
    for i in t:
        if i == "}":
            if s:
                s.pop()
            else:
                result += 1
                s.append("{")
        else:
            s.append(i)
    print(f"{n}. {result + len(s) // 2}")