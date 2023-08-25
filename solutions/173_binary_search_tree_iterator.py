from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = [root]
        curr = root
        while curr.left is not None:
            curr = curr.left
            self.stack.append(curr)

    def next(self) -> int:
        n = self.stack.pop()
        if n.right:
            self.stack.append(n.right)
            curr = n.right
            while curr.left is not None:
                curr = curr.left
                self.stack.append(curr)

        return n.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
