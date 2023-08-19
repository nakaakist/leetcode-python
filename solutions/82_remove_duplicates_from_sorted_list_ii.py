from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_pre_head = ListNode(float("-inf"), head)

        curr = head
        non_dup_head = dummy_pre_head
        prev = dummy_pre_head
        while curr:
            if not curr.next:
                if prev.val < curr.val:
                    non_dup_head.next = curr
                else:
                    non_dup_head.next = None
            elif prev.val < curr.val and curr.val < curr.next.val:
                non_dup_head.next = curr
                non_dup_head = curr

            prev, curr = curr, curr.next

        return dummy_pre_head.next


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


print_list(Solution().deleteDuplicates(make_list([0, 1, 1, 2, 4, 4])))
print_list(Solution().deleteDuplicates(make_list([])))
print_list(Solution().deleteDuplicates(make_list([0])))
