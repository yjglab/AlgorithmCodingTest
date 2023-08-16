import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline
def solution(n):
    if n == 3:
        return print(1)
    elif n == 4:
        return print(-1)
    table = [-1] * (n + 1)
    table[3], table[5] = 1, 1
    for i in range(6, n + 1):
        if table[i - 3] == -1 and table[i - 5] == -1:
            table[i] = -1
        elif table[i - 3] == -1 or table[i - 5] == -1:
            table[i] = max(table[i - 3], table[i - 5]) + 1
        else:
            table[i] = min(table[i - 3], table[i - 5]) + 1
    return print(table[n])
solution(int(input()))



