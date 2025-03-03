# STRETCH: implement Linear Search
def linear_search(arr, target):

    # TO-DO: add missing code
    for i in range(0, len(arr)):
        if (arr[i] == target):
            return i
    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    start = 0
    end = len(arr)-1
    middle = (start+end)//2

    # TO-DO: add missing code
    while (arr[middle] != target and start != middle):
        if (target < arr[middle]):
            end = middle
        else:
            start = middle

        middle = (start+end)//2

    if (arr[middle] == target):
        return middle
    elif (arr[end] == target):
        return end
    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search


def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls


print(binary_search([1, 2, 3, 4, 5], 5))
