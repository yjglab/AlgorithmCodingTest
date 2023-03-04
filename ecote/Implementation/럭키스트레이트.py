arr = list(map(int, input()))
print("LUCKY") if sum(arr[:len(arr) // 2]) == sum(arr[len(arr) // 2:]) else print("READY")
