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
        left = midpoint + 1
  return -1


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  midpoint = (low + high) // 2
  if len(arr) == 0:
    return -1 # array empty
  else:
    if arr[midpoint] == target:
      return midpoint
    elif low > high:
      return -1
    else:
      if target < arr[midpoint]:
        return binary_search_recursive(arr, target, low, midpoint - 1)
      else:
        return binary_search_recursive(arr, target, midpoint + 1, high)
