from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    ori_list = []
    for node in lists:
        while node:
            ori_list.append(node.val)
            node = node.next

    ori_list.sort()

    dummy = ListNode(0)
    current = dummy
    for val in ori_list:
        current.next = ListNode(val)
        current = current.next

    return dummy.next