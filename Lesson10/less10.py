arr = [1, 10, 6, 12, 0]
n = len(arr)
for i in range(n - 1):
    for j in range(n - 2, i - 1, -1):
        if arr[j+1] < arr[j]:
            arr[j+1], arr[j] = arr[j], arr[j+1]
print(arr)
