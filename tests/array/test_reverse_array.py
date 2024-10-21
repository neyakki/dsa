from pytest import mark

from dsa.array.reverse_array import reverse_array


@mark.parametrize(
    "arr,exp",
    [
        (
            [1, 2, 3, 4],
            [4, 3, 2, 1],
        ),
        (
            [1.0, 2.0, 3.0, 4.0],
            [4.0, 3.0, 2.0, 1.0],
        ),
        (
            [13, 101, 0, 1923],
            [1923, 0, 101, 13],
        ),
    ],
)
def test_reverse_array(arr, exp):
    reverse_array(arr)
    assert arr == exp, "The reverse array was created incorrectly"
