import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
from itertools import permutations

result = 0
for i in list(permutations(arr, n)):
    a = [abs(i[j] - i[j + 1]) for j in range(n - 1)]
    result = max(result, sum(a))
print(result)