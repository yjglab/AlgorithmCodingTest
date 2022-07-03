def solution(s): # 오답일 듯
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

# try 2
arr = [1, 0, 0, 1, 0, 0, 1, 1]
arr = list(map(int, input()))
def solution(target):
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == target:
           cnt += 1
           if i == len(arr) - 1:
               break
           if arr[i + 1] == target:
               cnt -= 1
    return cnt
print(min(solution(0), solution(1)))
