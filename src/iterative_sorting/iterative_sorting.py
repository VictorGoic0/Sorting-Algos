def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        current = arr[i]
        smallest = current
        smallest_index = i
        for j in range(i, len(arr)):
            if (arr[j] < smallest):
                smallest = arr[j]
                smallest_index = j
        arr[i], arr[smallest_index] = smallest, current
    return arr


def bubble_sort(arr):
    boolean = True
    while boolean:
        boolean = False
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                boolean = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr