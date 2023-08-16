import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
n_max = curr = numbers[0]

for i in range(1, n):
    curr += numbers[i]
    if curr > n_max:
        n_max = curr
    if numbers[i] > curr:
        n_max = max(n_max, numbers[i])
        curr = numbers[i]
print(n_max)

# dp
import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
table = [numbers[0]] + [0] * (n - 1)

for i in range(1, n):
    table[i] = max(numbers[i], table[i - 1] + numbers[i])
print(max(table))