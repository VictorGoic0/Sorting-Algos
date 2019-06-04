def merge(arrA, arrB):
    merged_arr = []
    while len(arrA) > 0 and len(arrB) > 0:
      if (arrA[0] < arrB[0]):
        merged_arr.append(arrA[0])
        arrA.pop(0)
      else:
        merged_arr.append(arrB[0])
        arrB.pop(0)
    while len(arrA) > 0:
      merged_arr.append(arrA[0])
      arrA.pop(0)
    while len(arrB) > 0:
      merged_arr.append(arrB[0])
      arrB.pop(0)
    return merged_arr

import math 
def merge_sort(arr):
  if (len(arr) <= 1):
    return arr
  else:
    midpoint = math.floor(len(arr) / 2)
    left = arr[0:midpoint]
    right = arr[midpoint:len(arr)]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
