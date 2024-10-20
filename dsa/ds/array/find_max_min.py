"""
find_max_min: Find maximum and minimum element in array
Author: Neyakki <neyakki@gmail.com>
=======
Task: Write a function that takes an array of numbers and returns
the minimum and maximum elements of the array.

Requirements:

    * Find the minimum and maximum values in one pass of the array.
"""

from typing import TypeVar

T = TypeVar("T", int, float)


def find_max_min(arr: list[T]) -> tuple[T, T]:
    """
    Find maximum and minimum element in array

    Args:
        arr: List of numbers (int, float).

    Returns:
        Maximum and minimum element
    """
    if not arr:
        return 0, 0

    _min = arr[0]
    _max = arr[0]

    for item in arr:
        if item > _max:
            _max = item
        elif item < _min:
            _min = item

    return _max, _min
