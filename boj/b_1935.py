import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
formula = list(input())
s = []
table = {}
for v in formula:
    if v.isalpha() and v not in table:
        table[v] = int(input())
for i, v in enumerate(formula):
    if v.isalpha():
        formula[i] = table[v]
for i in range(len(formula) - 1):
    if type(formula[i]) is int:
        s.append(formula[i])
    else:
        a, b = s.pop(), s.pop()
        s.append(eval(f"{b} {formula[i]} {a}"))
print(f"{s[0]:.2f}")
