import pytest
from problem_3.problem_3_solution import length_of_longest_substring


@pytest.mark.parametrize(
    "s, e",
    [
        ('abcabcbb', 3),
        ('bbbbb', 1),
        ('pwwkew', 3),
    ]
)
def test_problem_3_solution(s, e):
    r = length_of_longest_substring(s)
    assert r == e
