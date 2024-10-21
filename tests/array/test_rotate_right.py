from pytest import mark

from dsa.array.rotate_right import rotate_right


@mark.parametrize(
    "arr,k,exp",
    [
        (
            [1, 2, 3, 4],
            2,
            [3, 4, 1, 2],
        ),
        (
            [3, 2, 1, 4, 19],
            1,
            [19, 3, 2, 1, 4],
        ),
        (
            [1, 2, 6, 4],
            3,
            [2, 6, 4, 1],
        ),
        (
            [1, 2, 6, 4],
            4,
            [1, 2, 6, 4],
        ),
    ],
)
def test_rotate_right(arr, k, exp):
    rotate_right(arr, k)
    assert arr == exp, "The rotate array was incorrectly"
