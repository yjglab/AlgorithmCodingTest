def solution(x, y, n):
    table = [99] * (1000001)
    table[x] = 0
    if x == y:
        return 0

    for i in range(x, y):
        for new_n in (i + n, 2 * i, 3 * i):
            if 1000000 < new_n:
                continue
            table[new_n] = min(table[new_n], table[i] + 1)

    return table[y] if table[y] != 99 else -1