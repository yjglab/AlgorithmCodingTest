def solution(n, works):
    import heapq as hq
    q = []
    for i in works:
        hq.heappush(q, -i)
    for i in range(n):
        now = -hq.heappop(q)
        if not now:
            return 0
        hq.heappush(q, -(now - 1))
    result = 0
    for i in q:
        result += i ** 2
    return result