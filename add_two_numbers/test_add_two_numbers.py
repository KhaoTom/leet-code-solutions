import pytest
import add_two_numbers.add_two_numbers as a2n


@pytest.mark.parametrize(
    "source_list",
    [
        [],
        [0],
        [0, 1],
        [0, 1, 2],
    ]
)
def test_list_node_conversions(source_list):
    ln = a2n.make_list_node_from_list(source_list)
    l2 = a2n.make_list_from_list_node(ln)
    assert l2 == source_list
