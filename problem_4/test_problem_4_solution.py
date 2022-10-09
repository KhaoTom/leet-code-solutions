import pytest
from problem_4.problem_4_solution import find_median_sorted_arrays


@pytest.mark.parametrize(
    "list1, list2, expected_median",
    [
        ([], [], 0),
        ([], [5], 5),
        ([5], [], 5),
        ([1, 3], [2], 2),
        ([1, 2], [3, 4], 2.5),
        ([3, 5, 7, 12, 21, 23, 23, 23, 23, 29, 40], [13, 14, 56], 22),
        ([3, 13, 14, 21, 23, 23, 29, 39, 56], [5, 7, 12, 23, 23, 40], 23),
    ]
)
def test_problem_4_solution(list1, list2, expected_median):
    result = find_median_sorted_arrays(list1, list2)
    assert result == expected_median

