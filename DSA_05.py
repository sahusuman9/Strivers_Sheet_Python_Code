"""
write a program to rotate the elements of an array towards right by a given number of times.
"""

from typing import List
def rotate_array(arr: List[int], k: int) -> None:
    n = len(arr)
    k = k % n

    def reverse_array(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    reverse_array(0, n - 1)
    reverse_array(0, k - 1)
    reverse_array(k, n - 1)


array = list(map(int, input("Enter the elements of the array: ").split()))
k = int(input("Enter the number of times to rotate the array: "))
rotate_array(array, k)
print(array)
