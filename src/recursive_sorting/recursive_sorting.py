# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    a_index = b_index = 0
    for i in range(0, elements):
        # a empty, b not empty
        if a_index >= (len(arrA)):
            merged_arr[i] = arrB[b_index]
            b_index += 1
        # b empty, a not empty
        elif b_index >= (len(arrB)):
            merged_arr[i] = arrA[a_index]
            a_index += 1
        elif arrA[a_index] < arrB[b_index]:
            merged_arr[i] = arrA[a_index]
            a_index += 1
        elif arrB[b_index] <= arrA[a_index]:
            merged_arr[i] = arrB[b_index]
            b_index += 1
    return merged_arr



# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    # What is the base case?
    # if arr size is > 1? Return.
    if len(arr) > 1:
        # Split the arr in half until there are only one value in the arr. This is the base case.
        
        # Sort then add elements to the right
        left = merge_sort(arr[0:len(arr)//2])
        # Sort then add elements to the left
        right = merge_sort(arr[len(arr)//2:])

        # merge left and right
        arr = merge(left, right)

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # half is the first element in the right
    # half of the list
    half = mid + 1

    # If the two halves we're merging are already sorted, no need to do anything
    if arr[mid] <= arr[half]:
        return

    while start <= mid and half <= end:  # If element 1 is in right place
        if arr[start] <= arr[half]:
            start += 1
        else:
            value = arr[half]
            index = half
            # Shift all the elements between element 1
            # element 2, right by 1.
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1
            arr[start] = value
            # Update all the pointers
            start += 1
            mid += 1
            half += 1


def merge_sort_in_place(arr, l, r):
    # Your code here
    if l < r:
        m = l + (r - l) // 2
        # Sort first and second halves
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m+1, r)

        merge_in_place(arr,l,m,r)
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
