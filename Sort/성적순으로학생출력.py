n = int(input())
lst = []
for _ in range(n):
    a, b = list(input().split())
    lst.append((a, int(b)))
def func(lst):
    return lst[1]
result = sorted(lst, key=func)
for i in range(len(lst)):
    print(result[i][0], end=" ")