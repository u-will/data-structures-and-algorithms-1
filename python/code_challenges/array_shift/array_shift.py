def insertShiftArray(arr, n):
    mid = int(len(arr)/2)
    i = len(arr)
    arr.append(0)
    while(i > mid):
        arr[i] = arr[i-1]
        i = i-1
    arr[mid] = n
    return arr


print(insertShiftArray([1, 2, 3, 4], 5))
