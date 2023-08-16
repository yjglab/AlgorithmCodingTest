import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

def gcd_n(arr):
    def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a
    a = arr[0]
    for v in arr:
        a = gcd(a, v)
    return a

n, s = map(int, input().split())
arr = sorted([s] + list(map(int, input().split())))
diff = []
for i in range(1, n + 1):
    diff.append(arr[i] - arr[i - 1])
print(gcd_n([1, 3, 7, 11]))

# 내장 메서드 사용
import sys, math
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, s = map(int, input().split())
arr = sorted([s] + list(map(int, input().split())))
diff = []
result = arr[1] - arr[0]
for i in range(2, n + 1):
    result = math.gcd(result, arr[i] - arr[i - 1])
print(result)