import pytest
import problem_7.problem_7_solution as p7s


@pytest.mark.parametrize(
    "x, expected",
    [
        (0, 0),
        (-1, -1),
        (1, 1),
        (12, 21),
        (-12, -21),
        (123, 321),
        (-123, -321),
        (120, 21),
        (-120, -21),
        (-2147483648, 0),
        (2147483647, 0),
    ]
)
def test_problem_6_solution(x, expected):
    assert p7s.reverse_integer(x) == expected
