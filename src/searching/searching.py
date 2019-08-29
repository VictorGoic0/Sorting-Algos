# STRETCH: implement Linear Search				
def linear_search(arr, target):
  for i in range(len(arr)):
    elem = arr[i]
    if elem == target:
      return i
  return -1


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
  if len(arr) == 0:
    return -1 # array empty
  left = 0
  right = len(arr) - 1
  while left <= right:
    midpoint = (left + right) // 2
    if arr[midpoint] == target:
      return midpoint
    else:
      if target < arr[midpoint]:
        right = midpoint - 1
      else:
        left = midpoint+1
  return -1


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
