import sys
sys.stdin = open("input.txt", "r") # 제거
input = sys.stdin.readline

n = int(input())
init = [True if i == 1 else False for i in list(map(int, input().rstrip()))]
result = 100001
a, b = init[:], init[:]
b[0], b[1] = (not b[0]), (not b[1])
target = [True if i == 1 else False for i in list(map(int, input().rstrip()))]
def run(arr, cnt):
    for i in range(1, n):
        if arr[i - 1] != target[i - 1]:
            if i == n - 1:
                arr[i - 1], arr[i] = not arr[i - 1], not arr[i]
            else:
                arr[i - 1], arr[i], arr[i + 1] = not arr[i - 1], not arr[i], not arr[i + 1]
            cnt += 1
    if arr == target:
        return cnt
    return -1
for i, v in enumerate([a, b]):
    res = run(v, i)
    if res != -1:
        result = min(result, res)
print(-1 if result == 100001 else result)

