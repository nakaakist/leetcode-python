from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def pick_min(n1: Optional[ListNode], n2: Optional[ListNode]):
            if not n1 and not n2:
                return (None, None, None)
            v1 = n1.val if n1 else float("inf")
            v2 = n2.val if n2 else float("inf")
            return (n1, n1.next, n2) if v1 < v2 else (n2, n1, n2.next)

        head, n1, n2 = pick_min(list1, list2)
        curr = head
        while n1 or n2:
            curr.next, n1, n2 = pick_min(n1, n2)
            curr = curr.next

        return head


def make_list(vals: List[int]):
    vals.reverse()
    v = vals.pop()
    head = ListNode(v)
    curr = head
    while vals:
        v = vals.pop()
        curr.next = ListNode(v)
        curr = curr.next

    return head


def print_list(l: Optional[ListNode]):
    while l:
        print(l.val)
        l = l.next


print_list(Solution().mergeTwoLists(make_list([1, 2, 4]), make_list([1, 3, 4])))
