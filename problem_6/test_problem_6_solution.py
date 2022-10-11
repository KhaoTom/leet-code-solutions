import pytest

import problem_6.problem_6_solution as p6s


@pytest.mark.parametrize(
    "s, rows, expected",
    [
        ('A', 1, 'A'),
        ('AB', 1, 'AB'),
        ('ABC', 1, 'ABC'),
        ('ABCD', 1, 'ABCD'),
        ('ABCD', 2, 'ACBD'),
        ('PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR'),
        ('PAYPALISHIRING', 4, 'PINALSIGYAHRPI'),
    ]
)
def test_problem_6_solution(s, rows, expected):
    assert p6s.convert_to_zigzag_text(s, rows) == expected
