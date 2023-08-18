from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if head is None:
            return None

        ans_head = Node(head.val)
        ans_curr = ans_head
        curr = head
        ans_nodes = [ans_curr]
        node_indices = {}
        node_indices[curr] = 0
        i = 1
        while curr.next:
            curr = curr.next
            node_indices[curr] = i
            i += 1
            ans_curr.next = Node(curr.val)
            ans_curr = ans_curr.next
            ans_nodes.append(ans_curr)

        curr = head
        rand_nodes_indices = []
        while curr:
            rand_nodes_indices.append(node_indices[curr.random] if curr.random else -1)
            curr = curr.next

        for i, n in enumerate(ans_nodes):
            ind = rand_nodes_indices[i]
            n.random = ans_nodes[ind] if ind >= 0 else None

        return ans_head


def make_list(vals: List[int]):
    vals.reverse()
    v = vals.pop()
    head = Node(v)
    curr = head
    while vals:
        v = vals.pop()
        curr.next = Node(v)
        curr = curr.next

    return head


def print_list(l: Optional[Node]):
    while l:
        print(l.val)
        l = l.next


print_list(
    Solution().copyRandomList(
        make_list([1, 2, 4, 5, 6]),
    )
)
