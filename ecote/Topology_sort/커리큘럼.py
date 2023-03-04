n = int(input())
info = []
for _ in range(n):
    info.append(list(map(int, input().split())))
cost = [0] * (n + 1)
input_list = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for i in range(1, n + 1):
    cost[i] = info[i - 1][0]
    for j in range(len(info[i - 1])):
        input_list[i].append(info[i - 1][j])
        if info[i - 1][j] == -1:
            break

input_list = [x[1:-1] for x in input_list]
graph = [[] for _ in range(n + 1)]
for i in range(2, len(input_list)):
    for j in input_list[i]:
        graph[j].append(i)
        indegree[i] += 1

from collections import deque
q = deque()

def topology():
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    o_cost = cost[:]
    while q:
        poped = q.popleft()

        for i in graph[poped]:
            indegree[i] -= 1
            cost[i] = max(o_cost[i] + cost[poped], cost[i])
            if indegree[i] == 0:
                q.append(i)
topology()
for i in cost:
    print(i) if i else ""

'''
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
'''