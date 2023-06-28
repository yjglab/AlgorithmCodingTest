import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
table_a, table_b = [1] * n, [1] * n
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            table_a[i] = max(table_a[i], table_a[j] + 1)
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if arr[i] > arr[j]:
            table_b[i] = max(table_b[i], table_b[j] + 1)
result = 0
for i in range(n):
    result = max(result, table_a[i] + table_b[i] - 1)
print(result)

###

N = int(input())

List = list(map(int, input().split()))

dp1 = [1]*N
dp2 = [1]*N

sub_len=[0]*N

Max=0

for i in range(N):
    for j in range(i):
        if List[i] > List[j]:
            dp1[i] = max(dp1[i], dp1[j]+1)

List.reverse()

for i in range(N):
    for j in range(i):
        if List[i]>List[j]:
            dp2[i]=max(dp2[i],dp2[j]+1)
dp2.reverse()

for i in range(N):
    sub_len[i]=dp1[i]+dp2[i]

print(max(sub_len)-1)