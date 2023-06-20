def solution(n, s):
    if not s // n: 
        return [-1]
    arr = [s // n for _ in range(n)]
    for i in range(s % n):
        arr[i] += 1
    return sorted(arr)