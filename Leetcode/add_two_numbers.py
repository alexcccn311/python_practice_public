# 作者：Alex
# 2024/10/15 16:47
# Definition for singly-linked list.

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
class Solution:
    @staticmethod
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def linked_list_to_list(head):
            result_lst = []
            current = head
            while current:
                result_lst.append(current.val)
                current = current.next
            return result_lst

        def list_to_linked_list(lst):
            if not lst:
                return None
            head = ListNode(lst[0])
            current = head
            for value in lst[1:]:
                current.next = ListNode(value)
                current = current.next
            return head

        L1 = linked_list_to_list(l1)
        L2 = linked_list_to_list(l2)
        len_1, len_2 = len(L1), len(L2)
        num_1, num_2, num_3 = 0, 0, 0
        for i in range(len_1):
            result = L1[i] * 10 ** i
            num_1 += result

        for j in range(len_2):
            result = L2[j] * 10 ** j
            num_2 += result

        num_3 = num_1 + num_2
        list_3 = [int(x) for x in str(num_3)]
        l3 = list_3[::-1]
        return list_to_linked_list(l3)
"""

"""# Definition for singly-linked list.
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = None
        tail = None

        def append(val):
            nonlocal head, tail
            if head is None:
                head = ListNode(val % 10)
                tail = head
            else:
                tail.next = ListNode(val % 10)
                tail = tail.next

        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next

            append(val)  # 使用 append 函数处理

            carry = val // 10

        while carry:
            append(carry)  # 处理剩余的进位
            carry //= 10

        return head"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lista = ListNode()
        head = lista
        carry = 0
        while l1 != None or l2 != None:
            if l1.next == None and l2.next != None:
                l1.next = ListNode()
            if l2.next == None and l1.next != None:
                l2.next = ListNode()
            total =  (l1.val + l2.val + carry)
            lista.val = total%10
            carry = total // 10
            l1 = l1.next
            l2 = l2.next
            if l1 != None and l2 != None:
                lista.next = ListNode()
                lista = lista.next
        if carry:
            lista.next = ListNode(carry)
        return head