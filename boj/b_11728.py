import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, m = map(int, input().split())
a, b = list(map(int, input().split())), list(map(int, input().split()))
print(*sorted(a + b))