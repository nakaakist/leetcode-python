from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        curr = head
        while curr:
            curr = curr.next
            l += 1

        i = 0
        curr = head
        prev = None
        while curr:
            if i == l - n:
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next
                curr = curr.next
            else:
                prev, curr = curr, curr.next
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


print_list(Solution().removeNthFromEnd(make_list([0, 1, 2, 3, 4]), 2))
print_list(Solution().removeNthFromEnd(make_list([0, 1]), 2))
print_list(Solution().removeNthFromEnd(make_list([0, 1]), 1))
