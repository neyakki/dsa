from pytest import mark

from dsa.array.remove_duplicates import remove_duplicates


@mark.parametrize(
    "arr,exp",
    [
        (
            [1, 2, 2, 3, 3, 5, 4],
            [1, 2, 3, 5, 4],
        ),
        (
            [931, 129, 288, 129, 962, 348, 348, 40, 61, 61, 808],
            [931, 129, 288, 962, 348, 40, 61, 808],
        ),
        (
            ["ods", "tsw", "rews", "newss", "ods"],
            ["ods", "tsw", "rews", "newss"],
        ),
        ([], []),
    ],
)
def test_remove_duplicates(arr, exp):
    retval = remove_duplicates(arr)
    assert retval == exp, "The array contains duplicates"
