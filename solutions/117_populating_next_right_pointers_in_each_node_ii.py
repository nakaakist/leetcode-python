from collections import deque


# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return None

        queue = deque([root])

        while queue:
            queue.append(None)  # add sentinel
            while queue[0] is not None:
                n = queue.popleft()
                n.next = queue[0]
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
            queue.popleft()  # remove sentinel

        return root
