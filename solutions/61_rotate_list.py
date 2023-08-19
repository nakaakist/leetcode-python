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

        l = 0
        curr = head
        while curr:
            curr = curr.next
            l += 1

        k_rot = k % l

        if k_rot == 0:
            return head

        curr = head
        rot_head = None
        i = 0
        while curr:
            next = curr.next
            if i == l - k_rot - 1:
                curr.next = None
            if i == l - k_rot:
                rot_head = curr
            if i == l - 1:
                curr.next = head

            i += 1
            curr = next

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
