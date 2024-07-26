import pytest
from lab_1 import addition


@pytest.mark.parametrize(
    "x, y, result",
    [
        (2, 3, 5),
        (232, 334, 566),
        (-2, 3, 1),
        (0.2, 3, 3.2),
        (-2, -3, -5),
    ],
)
@pytest.mark.timeout(0.3)
def test_addition(x, y, result):
    assert addition(x, y) == result
