from pytest import mark

from dsa.array.find_max_min import find_max_min


@mark.parametrize(
    "arr,exp",
    [
        (
            [1, 2, 3, 4],
            (4, 1),
        ),
        (
            [13, 101, 0, 1923],
            (1923, 0),
        ),
        (
            [130, 403, 5013, 490, 384],
            (5013, 130),
        ),
        ([], (0, 0)),
        ([1], (1, 1)),
    ],
)
def test_find_max_min(arr, exp):
    max_min = find_max_min(arr)
    assert max_min == exp, "Incorrectly found max and min element"
