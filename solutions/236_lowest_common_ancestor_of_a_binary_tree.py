from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        path_so_far = []
        stack = [root]
        visited = defaultdict(bool)
        p1_dict = None

        while stack:
            node = stack[len(stack) - 1]
            if visited[node.val]:
                path_so_far.pop()
                stack.pop()
                continue

            visited[node.val] = True
            path_so_far.append(node)

            if node.val == p.val or node.val == q.val:
                if not p1_dict:
                    p1_dict = defaultdict(bool)
                    for n in path_so_far:
                        p1_dict[n.val] = True
                else:
                    while True:
                        n = path_so_far.pop()
                        if p1_dict[n.val] == True:
                            return n

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)


n2 = TreeNode(2)
n1 = TreeNode(1, None, n2)
n3 = TreeNode(3, n1)
n7 = TreeNode(7)
n6 = TreeNode(6, n7, n2)
n4 = TreeNode(4, None, n6)
n5 = TreeNode(5, n3, n4)


print(Solution().lowestCommonAncestor(n5, n6, n7))
