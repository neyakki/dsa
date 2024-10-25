from pytest import mark

from dsa.array.trap_rain_water import trap_rain_water


@mark.parametrize(
    "arr,exp",
    [
        (
            [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
            6,
        ),
        ([], 0),
        ([1], 0),
    ],
)
def test_trap_rain_water(arr, exp):
    sum_ = trap_rain_water(arr)
    assert sum_ == exp, "The amount was calculated incorrectly"
