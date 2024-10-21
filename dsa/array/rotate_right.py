"""
rotate_right: Rotate array to right
Author: Neyakki <neyakki@gmail.com>
=======
Task: Write a function that rotates the array to the right by a given
number of positions.

Requirements:

    * The array must be modified in place.
    * Implement an effective solution, for example, using multiple
    reversals.
"""

from typing import TypeVar

T = TypeVar("T")


def reverse_array(
    arr: list[T],
    start: int,
    end: int,
) -> None:
    """
    Reverse array in-place.

    Args:
        arr: List.
        start: Start index
        end: End index
    """
    while start < end - 1:
        arr[start], arr[end - 1] = arr[end - 1], arr[start]
        start += 1
        end -= 1


def rotate_right(arr: list[T], k: int) -> None:
    """
    Rotate array in-place.

    Args:
        arr: List.
        k: Count rotate
    """
    arr_size = len(arr)
    k %= arr_size

    reverse_array(arr, 0, arr_size)

    reverse_array(arr, 0, k)
    print(arr)
    reverse_array(arr, k, arr_size)
    print(arr)
