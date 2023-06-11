def solution(operations):
    import heapq
    maxh, minh = [], []
    for oper in operations:
        op, now = oper.split()
        if op == "I":
            heapq.heappush(maxh, -int(now))
            heapq.heappush(minh, int(now))
        elif op == "D":
            if len(maxh) == 0:
                pass
            elif now == "1":
                minh.remove(-heapq.heappop(maxh))
            elif now == "-1":
                maxh.remove(-heapq.heappop(minh))
    return [- heapq.heappop(maxh), heapq.heappop(minh)] if maxh else [0, 0]