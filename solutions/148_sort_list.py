from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_mid(head: Optional[ListNode]) -> Optional[ListNode]:
            if not head:
                return None

            fast = head
            slow_prev = None
            while fast is not None and fast.next is not None:
                fast = fast.next.next
                slow_prev = slow_prev.next if slow_prev else head
            slow = slow_prev.next
            slow_prev.next = None

            return slow

        def merge(h1: Optional[ListNode], h2: Optional[ListNode]) -> Optional[ListNode]:
            dummy_head = ListNode()
            curr = dummy_head
            while h1 is not None and h2 is not None:
                if h1.val <= h2.val:
                    curr.next = h1
                    h1, curr = h1.next, h1
                else:
                    curr.next = h2
                    h2, curr = h2.next, h2
            curr.next = h1 if h1 is not None else h2

            return dummy_head.next

        def sort(h: Optional[ListNode]) -> Optional[ListNode]:
            if h is None or h.next is None:
                return h
            mid = get_mid(h)
            h1 = sort(h)
            h2 = sort(mid)
            return merge(h1, h2)

        return sort(head)


def make_list(vals: list[int]):
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


print_list(Solution().sortList(make_list([4, 3, 2, 1])))
