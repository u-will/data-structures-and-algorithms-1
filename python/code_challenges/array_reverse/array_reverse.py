def reverse_array(arr):
    # initial left and right index assignment
    left = 0
    right = len(arr)-1

    # loop through the array and swap items
    while(left < right):
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    # return the reversed arraybw
    return arr


assert reverse_array([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1], "Fail"

assert reverse_array([7, 13, -19]) == [-19, 13, 7], "Fail"


print('*' * 80)
print('All tests passed')
print('*' * 80)
