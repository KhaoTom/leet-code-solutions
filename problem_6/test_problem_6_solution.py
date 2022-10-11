import pytest

import problem_6.problem_6_solution as p6s


@pytest.mark.parametrize(
    "s, rows, expected",
    [
        ('PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR'),
        ('PAYPALISHIRING', 4, 'PINALSIGYAHRPI'),
    ]
)
def test_problem_6_solution(s, rows, expected):
    assert p6s.convert_to_zigzag_text(s, rows) == expected
