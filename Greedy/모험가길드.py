n = int(input())
arr = list(map(int, input().split()))

def solution(n, arr):
    result, cnt, box = 0, 0, 0
    for x in arr:
        box = max(x, box)
        cnt += 1
        if cnt == box:
            cnt, box = 0, 0
            result += 1
            continue
    return result

print(solution(n, arr))