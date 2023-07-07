import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(input().rstrip()) for _ in range(n)]
b = [list(input().rstrip()) for _ in range(n)]
def trans(r, c, arr):
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            arr[i][j] = "1" if arr[i][j] == "0" else "0"
    if b == arr:
        return True
    return False
result, cnt = -1, 1
if a == b:
    print(0)
else:
    for i in range(n - 3 + 1):
        for j in range(m - 3 + 1):
            if a[i][j] != b[i][j]:
                if trans(i, j, a):
                    result = cnt
                cnt += 1
    print(result)