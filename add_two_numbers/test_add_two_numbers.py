import add_two_numbers.add_two_numbers as a2n


def test_make_list_node_from_list():
    l1 = a2n.make_list_node_from_list([1, 2, 3])
    assert l1.val == 1 and l1.next.val == 2 and l1.next.next.val == 3 and l1.next.next.next is None
