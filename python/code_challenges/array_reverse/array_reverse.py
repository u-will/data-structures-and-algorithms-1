def reverse_array(arr):
    # initial left and right index assignment
    l = 0
    r = len(arr)-1

    # loop through the array and swap items
    while(l<r):
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

    # return the reversed arraybw
    return arr


assert reverse_array([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1], "Fail"

assert reverse_array([7, 13, -19]) == [-19, 13, 7], "Fail"


print('*' * 80)
print('All tests passed')
print('*' * 80)
