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


def add_two_numbers(l1, l2):
    s = l1.val + l2.val
    carry = s // 10
    s = s % 10
    l1 = l1.next
    l2 = l2.next
    cln = ListNode(s)
    result = cln
    while True:
        if l1 and l2:
            s = l1.val + l2.val + carry
            carry = s // 10
            s = s % 10
            l1 = l1.next
            l2 = l2.next
            ln = ListNode(s)
            cln.next = ln
            cln = ln
        elif l1 and carry > 0:
            s = l1.val + carry
            carry = s // 10
            s = s % 10
            l1 = l1.next
            ln = ListNode(s)
            cln.next = ln
            cln = ln
        elif l2 and carry > 0:
            s = l2.val + carry
            carry = s // 10
            s = s % 10
            l2 = l2.next
            ln = ListNode(s)
            cln.next = ln
            cln = ln
        elif l1:
            cln.next = l1
            break
        elif l2:
            cln.next = l2
            break
        elif carry > 0:
            ln = ListNode(carry)
            cln.next = ln
            break
        else:
            break

    return result
