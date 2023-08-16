arr = list(map(int, input()))

def solution(arr):
    if len(arr) == 1:
        return arr[0]
    result = max(arr[0] + arr[1], arr[0] * arr[1])
    for i in range(2, len(arr)):
        if result + arr[i] < result * arr[i]:
            result *= arr[i]
        else:
            result += arr[i]
    return result
print(solution(arr))

# try 2
arr = list(map(int, input()))

def solution(arr):
    if len(arr) == 1:
        return arr[0]
    now = max(arr[0] + arr[1], arr[0] * arr[1])
    for i in range(2, len(arr)):
        now = max(now + arr[i], now * arr[i])
    return now
print(solution(arr))
