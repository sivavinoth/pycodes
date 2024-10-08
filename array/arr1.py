def func(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] = 1
        else:
            arr[i] = 1
    return arr


arr = [1, 1, 1, 1]
print(func(arr))
