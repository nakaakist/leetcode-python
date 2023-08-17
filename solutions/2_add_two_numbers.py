from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def calc_sum(l: Optional[ListNode]):
            s = 0
            n = l
            d = 0
            while n:
                s += n.val * 10**d
                n = n.next
                d += 1

            return s

        s = calc_sum(l1) + calc_sum(l2)

        head = ListNode(0)
        curr = head
        while s > 0:
            s, curr.val = divmod(s, 10)
            curr.next = ListNode(0) if s > 0 else None
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


print_list(
    Solution().addTwoNumbers(make_list([9, 9, 9, 9, 9, 9, 9]), make_list([9, 9, 9, 9]))
)
print_list(Solution().addTwoNumbers(make_list([2, 4, 3]), make_list([5, 6, 4])))
print_list(Solution().addTwoNumbers(make_list([0]), make_list([0])))
