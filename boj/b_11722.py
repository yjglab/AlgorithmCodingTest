import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
print(arr)
table = [1] * n
for i in range(n):
    for j in range(i):
        if arr[i] < arr[j]:
            table[i] = max(table[i], table[j] + 1)
print(max(table))
