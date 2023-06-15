def solution(a, b):
    a.sort()
    b.sort()
    ai, result = 0, 0
    
    for bi in range(len(b)):
        if a[ai] < b[bi]:
            result += 1
            ai += 1
    return result