from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def __init__(self):
        self.visited = {}

    def getClonedNode(self, node):
        if node:
            if node in self.visited:
                return self.visited[node]
            else:
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]
        return None

    def copyRandomList(self, head):
        if not head:
            return head

        old_node = head
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node

        while old_node != None:
            new_node.random = self.getClonedNode(old_node.random)
            new_node.next = self.getClonedNode(old_node.next)

            old_node = old_node.next
            new_node = new_node.next

        return self.visited[head]


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
