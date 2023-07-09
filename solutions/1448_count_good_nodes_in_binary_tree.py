# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        nodes = [(root, float("-inf"))]

        num_good_nodes = 0
        while nodes:
            node, max_so_far = nodes.pop()
            if not node:
                continue

            if node.val >= max_so_far:
                num_good_nodes += 1
                nodes.append((node.left, node.val))
                nodes.append((node.right, node.val))
            else:
                nodes.append((node.left, max_so_far))
                nodes.append((node.right, max_so_far))

        return num_good_nodes


n1 = TreeNode(3)
n2 = TreeNode(2)
n3 = TreeNode(3, n1, n2)
n4 = TreeNode(5)
n5 = TreeNode(5, n3, n4)


print(Solution().goodNodes(n5))
