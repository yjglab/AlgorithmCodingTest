def solution(stk):
    n = len(stk)
    if n <= 3:
        return max(stk)
    if n == 4:
        return max(stk[0] + stk[2], stk[1] + stk[3])
    t1 = stk[1:]
    t2 = stk[:-1]
    t1[2] += t1[0]
    t2[2] += t2[0]
    
    for i in range(3, len(t1)):
        t1[i] += max(t1[i - 2], t1[i - 3])
        t2[i] += max(t2[i - 2], t2[i - 3])
    t1, t2 = max(t1), max(t2)
    return max(t1, t2)