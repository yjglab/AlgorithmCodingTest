def solution(routes):
    last, result = -30001, 0
    for r in sorted(routes, key = lambda x: x[1]):
        if last < r[0]:
            result += 1
            last = r[1]
    return result
    