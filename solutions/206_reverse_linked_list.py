from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next

        return prev


n1 = ListNode(5)
n2 = ListNode(4, n1)
n3 = ListNode(3, n2)
n4 = ListNode(2, n3)
n5 = ListNode(1, n4)

head = Solution().reverseList(n5)

curr = head
while curr is not None:
    print(curr.val)
    curr = curr.next
