# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        current = arr[i]
        smallest = current
        smallest_index = i
        for j in range(i, len(arr)):
            if (arr[j] < smallest):
                smallest = arr[j]
                smallest_index = j
        arr[i] = smallest
        arr[smallest_index] = current
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr