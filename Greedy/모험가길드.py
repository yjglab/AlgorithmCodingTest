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

# try 2
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
# 3 2 2 2 1
result, max_count = 0, 0
group = []
for i in range(n):
    max_count = max(max_count, arr[i])
    group.append(arr[i])
    if len(group) == max_count:
        max_count = 0
        result += 1
        group = []
print(result)