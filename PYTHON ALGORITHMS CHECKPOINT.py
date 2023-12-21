#!/usr/bin/env python
# coding: utf-8

# In[1]:


def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return True
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return False

# Test cases
result1 = binary_search([1, 2, 3, 5, 8], 6)
result2 = binary_search([1, 2, 3, 5, 8], 5)

print(result1)  # Output: False
print(result2)  # Output: True


# ### Python program to calculate the value of 'a' to the power of 'b' 

# In[2]:


def power(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result

# Test case
result = power(3, 4)
print(result)  # Output: 81


# ### Python program to sort a list of elements using bubble sort algorithm

# In[3]:


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Sample data
data = [29, 13, 22, 37, 52, 49, 46, 71, 56]

# Sorting the list using bubble sort
bubble_sort(data)

# Displaying the sorted list
print("Sorted Result:", data)


# ### Python program to sort a list of elements using the merge sort algorithm

# In[4]:


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check for any remaining elements in left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Check for any remaining elements in right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Sample data
data = [29, 13, 22, 37, 52, 49, 46, 71, 56]

# Sorting the list using merge sort
merge_sort(data)

# Displaying the sorted list
print("Sorted Result:", data)


# ### Python program to sort a list of elements using the quick sort algorithm

# In[5]:


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Sample data
data = [29, 13, 22, 37, 52, 49, 46, 71, 56]

# Sorting the list using quick sort
sorted_data = quick_sort(data)

# Displaying the sorted list
print("Sorted Result:", sorted_data)


# In[ ]:




