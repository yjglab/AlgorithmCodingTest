import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    print(" ".join(list(map(lambda x: "".join(reversed(x)), input().split()))))
