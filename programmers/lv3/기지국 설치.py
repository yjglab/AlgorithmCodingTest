def solution(n, stations, w):
    from collections import deque
    q = deque(stations)
    now, result = 1, 0
    while 1:
        if now > n:
            break
        if q:
            if now >= q[0] - w and now <= q[0] + w:
                now = q.popleft() + w + 1
                continue
            if now + w < q[0] - w:
                now += w
            now += w + 1
        else:
            if now + w > n:
                result += 1
                break
            now += w * 2 + 1    
        result += 1
    return result