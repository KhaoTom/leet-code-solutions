import pytest
from problem_5.problem_5_solution import longest_palindrome


@pytest.mark.parametrize(
    "given_string, expected_palindrome",
    [
        ('s', 's'),
        ('babad', 'bab'),
        ('cbbd', 'bb'),
        ('abacabba', 'bacab'),
    ]
)
def test_problem_5_solution(given_string, expected_palindrome):
    result = longest_palindrome(given_string)
    assert result == expected_palindrome
