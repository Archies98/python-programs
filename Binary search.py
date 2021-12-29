# Binary Search Algorithm Implementation in Python 

# Binary search is one of the most common algorithms for finding items in sequential data types such as a list. 
# Here is a good introduction and pseudo-code for this algorithm. Write a function in Python that takes a list of integers, 
# and a specific integer and uses binary search to find if the desired integer is present in the list. 
# If the integer is present, the function will return True, otherwise, it will return False

def binary_search(int_list, num_to_search):
  int_list = sorted(int_list)
  low = 0
  high = len(int_list) - 1
  mid = 0
 
  while low <= high:
 
      mid = (high + low) // 2
 
      # If required number is greater, ignore left half
      if int_list[mid] < num_to_search:
          low = mid + 1
 
      # If required number is smaller, ignore right half
      elif int_list[mid] > num_to_search:
          high = mid - 1
 
      # required number is found
      else:
          return True
 
  # If we reach here, then the required number was not in the list
  return False

# testing our binary search implementation
print(f"8 in list [1,2,3,4,5,6,7,8,9,10]: {binary_search([1,2,3,4,5,6,7,8,9,10], 8)}")
print(f"100 in list [100,2,34,4,5,600,7,8,9,10]: {binary_search([100,2,34,4,5,600,7,8,9,10], 100)}")
print(f"77 in list [10,82,323,454,50,668,78,80,9,108]: {binary_search([10,82,323,454,50,668,78,80,9,108], 77)}")