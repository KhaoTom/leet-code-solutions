import pytest
import problem_2.problem_2_solution as p2s


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
    ln = p2s.make_list_node_from_list(source_list)
    l2 = p2s.make_list_from_list_node(ln)
    assert l2 == source_list


@pytest.mark.parametrize(
    "l1, l2, e",
    [
        ([0], [0], [0]),
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ]
)
def test_add_two_numbers(l1, l2, e):
    ln1 = p2s.make_list_node_from_list(l1)
    ln2 = p2s.make_list_node_from_list(l2)
    r = p2s.add_two_numbers(ln1, ln2)
    rl = p2s.make_list_from_list_node(r)
    assert rl == e
