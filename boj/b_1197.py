import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

result = 0
v, e = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(e)]
parent = [-1] + [i for i in range(1, v + 1)]

def findP(x):
    if parent[x] != x:
        return findP(parent[x])
    return x
def union(a, b):
    if findP(a) > findP(b):
        parent[a] = b
    else:
        parent[b] = a

for a, b, c in sorted(edges, key=lambda x: x[2]):
    a, b = findP(a), findP(b)
    if a != b:
        union(a, b)
        result += c
print(result)
