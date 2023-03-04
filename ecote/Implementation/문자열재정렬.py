arr = list(input())
arr.sort()
idx, digit = 0, 0

if any(map(str.isdigit, arr)):
    for i in arr:
        if i.isdigit():
            idx += 1
            digit += int(i)
    arr = arr[idx:]
    arr.append(digit)

for i in arr:
    print(i, end="")