n, m = map(int, input().split())
lst = list(map(int, input().split()))

def bs(stt, end):
    result = 0
    while stt <= end:
        mid = (stt + end) // 2
        remain = sum([i - mid if i - mid > 0 else 0 for i in lst])
        if remain > m:
            stt = mid + 1
        elif remain <= m:
            result = mid
            end = mid - 1
    return result

print(bs(0, max(lst)))