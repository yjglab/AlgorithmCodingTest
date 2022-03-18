def solution(s):
    c = 0
    if s.count(0) < s.count(1):
        c = 0
    else:
        c = 1
    start = s.index(c)
    sig = 0 if s[start] == 1 else 1
    
    result = 1
    for i in range(start, len(s)):
        if s[i] != sig:
            s[i] = sig
        else:
            break
    print(s)
    if s.count(sig) == len(s):
        return result
    else:
        return result + solution(s)

s = list(map(int, input()))
print(solution(s))