"""
Q1. Write a python program to find the largest element in an array.
"""
from typing import List
def find_largest_element(n: int, arr: List[int]) -> int:
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max


array = list(map(int, input("Enter the elements of the array: ").split()))
print("The largest element in the array is: ", find_largest_element(len(array), array))

"""
Time Complexity: O(n) where n is the number of elements in the array; uses only one for loop.
Space Complexity: O(1) as we are using only a constant amount of extra space.
"""