"""
4. Write a Python program to remove duplicates from a sorted array or list.
"""

from typing import List
def remove_duplicates(arr: List[int]) -> List[int]:
    if not arr:
        return 0
    k = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[k - 1]:
            arr[k] = arr[i]
            k += 1
    return k 


array = list(map(int, input("Enter the elements of the sorted array: ").split()))
print("Array size after removing duplicates: ", remove_duplicates(array))