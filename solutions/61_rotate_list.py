from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        l = 1
        tail = head
        while tail.next:
            tail = tail.next
            l += 1
        tail.next = head

        curr = head
        for _ in range(l - k % l - 1):
            curr = curr.next

        rot_head = curr.next
        curr.next = None

        return rot_head


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


# print_list(Solution().rotateRight(make_list([0, 1, 2, 3, 4, 5]), 5))
print_list(Solution().rotateRight(make_list([0, 1, 2]), 1))
