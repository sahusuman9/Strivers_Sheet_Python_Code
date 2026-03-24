"""
3. Write a program to check if the array is sorted (Rotation and Sorting)
"""

from typing import List
def is_sorted(arr: List[int]) -> bool:
    n = len(arr)
    if n == 1:
        return True
    count = 0

    for i in range(n):
        if arr[i] > arr[(i + 1) % 5]:
            count += 1
    return count <= 1

array = list(map(int, input("Enter the elements of the array: ").split()))
print("Is the array sorted and rotated sorted? ", is_sorted(array))

"""
Time Complexity: O(n) where n is the number of elements in the array; uses only one for loop.
Space Complexity: O(1) as we are using only a constant amount of extra space.
"""