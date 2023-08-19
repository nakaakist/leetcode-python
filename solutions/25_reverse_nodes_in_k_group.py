from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        def reverse(start: ListNode, end: ListNode):
            curr = start
            prev = None
            while prev != end:
                next = curr.next
                curr.next = prev
                curr, prev = next, curr

        curr = head
        prev_group_start = None
        group_start = None
        i = 0
        while curr:
            next = curr.next
            if (i + 1) % k == 0:
                if i == k - 1:
                    head = curr
                if prev_group_start:
                    prev_group_start.next = curr
                reverse(group_start, curr)
            elif i % k == 0:
                prev_group_start, group_start = group_start, curr
                if prev_group_start:
                    prev_group_start.next = curr

            curr = next
            i += 1

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


# print_list(Solution().reverseBetween(make_list([1, 2, 3, 4, 5]), 2, 4))
# print_list(Solution().reverseBetween(make_list([5]), 1, 1))
print_list(Solution().reverseKGroup(make_list([0, 1, 2, 3, 4, 5, 6]), 4))
print_list(Solution().reverseKGroup(make_list([0, 1, 2, 3, 4]), 2))
print_list(Solution().reverseKGroup(make_list([0, 1]), 1))
print_list(Solution().reverseKGroup(make_list([1]), 2))
