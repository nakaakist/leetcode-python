from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        elif head.next is None:
            return head

        even_head = head.next
        curr = head
        is_curr_odd = True
        while True:
            next = curr.next
            if next.next is None:
                if is_curr_odd:
                    curr.next = even_head
                else:
                    curr.next = None
                    next.next = even_head
                break
            else:
                curr.next = next.next

            curr = next
            is_curr_odd = not is_curr_odd

        return head


n1 = ListNode(5)
n2 = ListNode(4, n1)
n3 = ListNode(3, n2)
n4 = ListNode(2, n3)
n5 = ListNode(1, n4)

head = Solution().oddEvenList(n5)

curr = head
while curr is not None:
    print(curr.val)
    curr = curr.next
