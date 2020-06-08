# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    print(merged_arr)
    # Sorting happens here...
    # Place element 0 in arrA
    a = 0
    b = 0

    for c in range(0, elements):
        # start comparisons
        # If a is out of range, push b and iterate.
        if a >= len(arrA):
            # we're done with a, push b
            merged_arr[c] = arrB[b]
            b += 1
        # If b is out of range, push a and iterate.
        elif b >= len(arrB):
            merged_arr[c] = arrA[a]
            a += 1
        # If a is smaller place into merged_arr at index c and iterate both.
        elif arrA[a] < arrB[b]:
            merged_arr[c] = arrA[a]
            a += 1
        # If b is smaller place into merged_arr at index c and iterate both.
        elif arrA[a] > arrB[b]:
            merged_arr[c] = arrB[b]
            b += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here

    # What is the base case?
    # if arr size is > 1? Return.
    if len(arr) > 1:
        # Split the array in half until there are only one values in the array. This is the base case.
        # Sort then Add elements to the right
        left = merge_sort(arr[0:len(arr)//2])
        # Sort then Add elements to the left
        right = merge_sort(arr[len(arr)//2:])

        # merge left and right
        arr = merge(left, right)

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # start2 is the first element in the right

    # half of the list
    start2 = mid + 1

    # If the two halves we're merging are already
    # sorted, no need to do anything
    if arr[mid] <= arr[start2]:
        return

    # Two pointers to maintain start
    # of both arrays to merge
    while start <= mid and start2 <= end:  # If element 1 is in right place
        if arr[start] <= arr[start2]:
            start += 1
        else:
            value = arr[start2]
            index = start2
            # Shift all the elements between element 1
            # element 2, right by 1.
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1
            arr[start] = value
            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1    


    return arr


def merge_sort_in_place(arr, l, r):
    if l < r:
        # Same as (l + r) / 2, but avoids overflow
        # for large l and r
        m = l + (r - l) // 2
        # Sort first and second halves
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)
        merge_in_place(arr, l, m, r)


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
