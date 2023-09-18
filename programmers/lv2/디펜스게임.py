import heapq
def solution(n, k, enemy):
    if k >= len(enemy):
        return len(enemy)
    hq = []
    
    for i in range(len(enemy)):
        heapq.heappush(hq, enemy[i])
        if len(hq) > k:
            last = heapq.heappop(hq)
            if last > n:
                return i
            n -= last
    return len(enemy)