"""
max_subarray_sum: Calculating the maximum amount of a subarray
=======
Task: The height of each column is given as an array of numbers.
Write a function that calculates how many units of water can be
"trapped" between columns after rain.

Requirements:

    * Implement a solution with optimal complexity O(n).
"""


def trap_rain_water(arr: list[int]) -> int:
    """
    Calculates how many units of water can be "trapped"
    between columns after rain

    Args:
        arr: List of int.

    Returns:
        Sum
    """
    if not arr:
        return 0

    left, right = 0, len(arr) - 1
    left_max, right_max = arr[left], arr[right]
    water_trapped = 0

    while left < right:
        if arr[left] < arr[right]:
            if arr[left] >= left_max:
                left_max = arr[left]
            else:
                water_trapped += left_max - arr[left]
            left += 1
        else:
            if arr[right] >= right_max:
                right_max = arr[right]
            else:
                water_trapped += right_max - arr[right]
            right -= 1

    return water_trapped
