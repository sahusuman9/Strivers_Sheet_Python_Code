"""
2. Write a Python program to find the second largest number in a list.
"""

from typing import List
def find_second_largest(num: int, arr: List[int]) -> int:
    largest = sec_largest = -1
    for num in arr:
        if num > largest:
            sec_largest = largest
            largest = num
        elif num > sec_largest and num != largest:
            sec_largest = num
    return sec_largest


array = list(map(int, input("Enter the elements of the array: ").split()))
print("The second largest element in the array is: ", find_second_largest(len(array), array))


"""
Time Complexity: O(n) where n is the number of elements in the array; uses only one for loop.
Space Complexity: O(1) as we are using only a constant amount of extra space.
"""