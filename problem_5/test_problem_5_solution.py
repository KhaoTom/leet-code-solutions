import pytest
from problem_5.problem_5_solution import longest_palindrome, find_longest_palindrome_starting_with_last_value


@pytest.mark.parametrize(
    "given_string, expected_palindrome",
    [
        ('s', 's'),
        ('babab', 'babab'),
        ('cadcbc', 'cbc'),
        ('abacabba', 'abba'),
    ]
)
def test_find_longest_palindrome_starting_with_last_value(given_string, expected_palindrome):
    result = find_longest_palindrome_starting_with_last_value(given_string)
    assert result == expected_palindrome


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
