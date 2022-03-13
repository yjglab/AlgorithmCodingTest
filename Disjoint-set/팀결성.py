n, m = map(int, input().split())
parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
for _ in range(m):
    sig, a, b = map(int, input().split())
    
    if sig == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
    elif sig == 0:
        union_parent(parent, a, b)
        