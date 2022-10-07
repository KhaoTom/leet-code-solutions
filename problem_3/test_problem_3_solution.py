import pytest
from problem_3.problem_3_solution import length_of_longest_substring


@pytest.mark.parametrize(
    "s, e",
    [
        ('', 0),
        ('abcabcbb', 3),
        ('bbbbb', 1),
        ('pwwkew', 3),
        ('dvdf', 3),
        ('123456789101112131415', 10)
    ]
)
def test_problem_3_solution(s, e):
    r = length_of_longest_substring(s)
    assert r == e
