import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
arr = [list(input().split()) for _ in range(n)]
direction = ((-1, 0), (1, 0), (0, -1), (0, 1))
t = 0
result = "NO"
for i in arr:
    t += i.count("T")

def setting(o):
    global result
    def finded(r, c):
        for [p, q] in direction:
            dr, dc = r + p, c + q
            while 1:
                if dr < 0 or dc < 0 or dr >= n or dc >= n or arr[dr][dc] == "O":
                    break
                if arr[dr][dc] == "S":
                    return 1
                dr, dc = dr + p, dc + q
        return 0
    if o == 3:
        checked = 0
        for i in range(n):
            for j in range(n):
                if arr[i][j] == "T" and not finded(i, j):
                        checked += 1
        if checked == t:
            result = "YES"
        return
    for i in range(n):
        for j in range(n):
            if arr[i][j] == "X":
                arr[i][j] = "O"
                setting(o + 1)
                arr[i][j] = "X"
setting(0)
print(result)