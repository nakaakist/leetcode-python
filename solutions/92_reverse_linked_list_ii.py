from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        pre = None
        start = None
        end = None
        post = None
        prev = None

        curr = head
        i = 0
        while curr:
            next = curr.next
            if i == left - 2:
                pre = curr
            if i == left - 1:
                start = curr
            if i > left - 1 and i <= right - 1:
                curr.next = prev
            if i == right - 1:
                end = curr
            if i == right:
                post = curr

            prev = curr
            curr = next
            i += 1

        if pre is not None:
            pre.next = end
        start.next = post

        if left > 1:
            return head
        else:
            return end


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


# print_list(Solution().reverseBetween(make_list([1, 2, 3, 4, 5]), 2, 4))
# print_list(Solution().reverseBetween(make_list([5]), 1, 1))
print_list(Solution().reverseBetween(make_list([3, 5]), 1, 2))
print_list(Solution().reverseBetween(make_list([3, 5]), 2, 2))
