arr = list(map(int, input()))

def solution(result, arr):
    if len(arr) == 1:
        return arr[0]
    result = max(arr[0] + arr[1], arr[0] * arr[1])
    for i in range(2, len(arr)):
        if result + arr[i] < result * arr[i]:
            result *= arr[i]
        else:
            result += arr[i]
    return result
print(solution(result, arr))