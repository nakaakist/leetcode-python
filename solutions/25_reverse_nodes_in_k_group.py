from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseLinkedList(self, head, k):
        prev, curr = None, head
        while k:
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
            k -= 1

        return prev

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count = 0
        ptr = head

        while count < k and ptr:
            ptr = ptr.next
            count += 1

        if count == k:
            rev_head = self.reverseLinkedList(head, k)
            head.next = self.reverseKGroup(ptr, k)
            return rev_head
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
