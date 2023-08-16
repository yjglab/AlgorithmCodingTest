def solution(n, t, m, p):
    import string
    tmp = string.digits + string.ascii_uppercase
    def convert(num, base) :
        q, r = divmod(num, base)
        if q == 0 :
            return tmp[r] 
        else :
            return convert(q, base) + tmp[r]
    converted = ""
    for i in range(t * m):
        converted += convert(i, n)
    return "".join([converted[i] for i in range(p - 1, t * m, m)])
    