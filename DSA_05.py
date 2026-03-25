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


"""
Time Complexity:  (Linear)The code performs three reversal operations. Each reversal visits every element in its range exactly once to perform a swap.Total work:  (first reverse) +  (second reverse) +  (third reverse) =  operations.In Big O notation, constants are dropped, resulting in . This is the best possible time complexity because every element must be moved to a new position.
Space Complexity:  (Constant)The rotation is performed in-place.It only uses a few integer variables (n, k, start, end) regardless of how large the input array is.No auxiliary arrays or large data structures are created, making it highly memory-efficient.
"""
