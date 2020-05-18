# TO-DO: Complete the selection_sort() function below
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
                
        # TO-DO: swap
        # Your code here
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr



# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Iterate through the array
    for i in range(0, len(arr) - 1):
        # Iterate again and subtract the last item 
        # Since it's already sorted
        for j in range(0, len(arr) - 1 - i):
            # If a number in lower index is higher
            # Than the next index
            if arr[j] > arr[j + 1]:
                # Swap them
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr


print(selection_sort(arr1))
