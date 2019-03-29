def find_uniq(arr):
    '''
    There is an array with some numbers. All numbers are equal except for one. Try to find it!
    '''
    arr.sort()

    if arr.count(arr[0]) == 1:
        return arr[0]
    else:
        return arr[-1]
