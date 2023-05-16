import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
d = [0, 9, 189, 2889, 38889, 488889, 5888889, 68888889, 788888889]
nlen = len(str(n))
print(d[nlen - 1] + nlen * ((n - 10 ** (nlen - 1)) + 1))