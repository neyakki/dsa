"""
remove_duplicates: Remove duplicates items from array
Author: Neyakki <neyakki@gmail.com>
=======
Task: Write a function that removes all duplicates from the array and
returns a new array with unique elements. The order of the elements
must be preserved.

Requirements:

    * Do not use built-in data structures such as set.
"""

from typing import TypeVar

T = TypeVar("T")


def remove_duplicates(arr: list[T]) -> list[T]:
    """
    Remove duplicates items from array

    Args:
        arr: List.

    Returns:
        New list without duplicates
    """
    _arr_without_duplicates: list[T] = []

    if not arr:
        return _arr_without_duplicates

    for item in arr:
        if item not in _arr_without_duplicates:
            _arr_without_duplicates.append(item)

    return _arr_without_duplicates
