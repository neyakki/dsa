"""
max_subarray_sum: Calculating the maximum amount of a subarray
=======
Task: Write a program that finds a subarray with the maximum sum of
elements in a given array of integers (including negative ones).
Implement the Kadane algorithm.

Requirements:

    * Return the sum of the subarray elements with the maximum amount.
"""

from typing import TypeVar

T = TypeVar("T", int, float)


def max_subarray_sum(arr: list[T]) -> T:
    """
    Calculating the maximum amount of a subarray

    Args:
        arr: List.

    Returns:
        Sum
    """
    if not arr:
        return 0

    local_max = arr[0]
    global_max = arr[0]

    for num in arr[1:]:
        local_max = max(num, local_max + num)
        global_max = max(local_max, global_max)

    return global_max
