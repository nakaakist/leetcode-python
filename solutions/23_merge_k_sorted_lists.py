import heapq
from typing import List, Optional, Tuple


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists_heap = [(n.val, i, n) for i, n in enumerate(lists) if n is not None]
        if len(lists_heap) == 0:
            return None

        heapq.heapify(lists_heap)

        def pop_min(
            lists_heap: List[Tuple[int, int, ListNode]], ans_curr: Optional[ListNode]
        ):
            _, i, n = heapq.heappop(lists_heap)
            if ans_curr:
                ans_curr.next = n
            if n.next:
                heapq.heappush(lists_heap, (n.next.val, i, n.next))

            return n

        ans_head = pop_min(lists_heap, None)
        ans_curr = ans_head
        while len(lists_heap) > 0:
            ans_curr = pop_min(lists_heap, ans_curr)

        return ans_head


print(Solution().mergeKLists([ListNode(2), ListNode(1), ListNode(1)]))
