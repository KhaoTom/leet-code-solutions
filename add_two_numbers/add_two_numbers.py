class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def make_list_node_from_list(source_list):
    if not source_list:
        return None

    if len(source_list) == 1:
        return ListNode(source_list[0])

    list_nodes = [ListNode(v) for v in source_list]

    for i in range(len(list_nodes) - 1):
        list_nodes[i].next = list_nodes[i+1]

    return list_nodes[0]


def make_list_from_list_node(list_node):
    if not list_node:
        return []

    result = [list_node.val]
    while list_node.next is not None:
        list_node = list_node.next
        result.append(list_node.val)

    return result
