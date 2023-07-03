import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
numbers = list(input().split())
obj = {}
for i in numbers:
    obj[i] = 1

m = int(input())
arr = list(input().split())
for i in arr:
    if i in obj:
        print(1, end=" ")
    else:
        print(0, end=" ")