from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        if len(nodes) == 1:
            return None

        i_delete = len(nodes) // 2
        n_before = nodes[i_delete - 1]

        n_before.next = n_before.next.next

        return head


n1 = ListNode(6)
n2 = ListNode(2, n1)
n3 = ListNode(1, n2)
n4 = ListNode(7, n3)
n5 = ListNode(4, n4)
n6 = ListNode(3, n5)
n7 = ListNode(1, n6)

head = Solution().deleteMiddle(n7)


curr = head
while curr is not None:
    print(curr.val)
    curr = curr.next
