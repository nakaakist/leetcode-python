from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l_head = ListNode(float("-inf"))
        l_tail = l_head
        g_head = ListNode(float("inf"))
        g_tail = g_head
        curr = head
        while curr:
            if curr.val < x:
                l_tail.next = curr
                l_tail = curr
            else:
                g_tail.next = curr
                g_tail = curr
            curr = curr.next

        g_tail.next = None
        l_tail.next = g_head.next

        return l_head.next
