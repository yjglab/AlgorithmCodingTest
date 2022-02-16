import sys
n = int(sys.stdin.readline().rstrip())
items = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
needs = list(map(int, sys.stdin.readline().rstrip().split()))

def bs(stt, end, target):
    while stt <= end:
        mid = (stt + end) // 2
        if items[mid] == target:
            return "yes"
        elif items[mid] > target:
            end = mid - 1
        elif items[mid] < target:
            stt = mid + 1
    return "no"
for i in range(m):
    print(bs(0, len(items) - 1, needs[i]), end=" ")