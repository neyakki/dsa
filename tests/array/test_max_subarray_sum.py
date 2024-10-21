from pytest import mark

from dsa.array.max_subarray_sum import max_subarray_sum


@mark.parametrize(
    "arr,exp",
    [
        (
            [-2, 1, -3, 4, -1, 2, 1, -5, 4],
            6,
        ),
        ([], 0),
    ],
)
def test_max_subarray_sum(arr, exp):
    retval = max_subarray_sum(arr)
    assert retval == exp, "The amount is not calculated correctly"
