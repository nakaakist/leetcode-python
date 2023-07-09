from collections import deque
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast:
            slow = slow.next
            fast = fast.next.next

        prev, rev_head = None, slow
        while rev_head:
            next = rev_head.next
            rev_head.next = prev

            prev = rev_head
            rev_head = next

        max = 0
        curr, rev_curr = head, prev
        while rev_curr:
            sum = curr.val + rev_curr.val
            if sum > max:
                max = sum

            curr = curr.next
            rev_curr = rev_curr.next

        return max


n1 = ListNode(6)
n2 = ListNode(2, n1)
n3 = ListNode(1, n2)
n4 = ListNode(7, n3)
n5 = ListNode(4, n4)
n6 = ListNode(3, n5)

print(Solution().pairSum(n6))
