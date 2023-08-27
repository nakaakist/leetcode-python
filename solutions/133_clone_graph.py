# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return None

        root_copy = Node(node.val)
        root = node

        stack = [root]
        copied_nodes = {root: root_copy}

        while stack:
            n = stack.pop()
            n_copy = copied_nodes[n]
            for nb in n.neighbors:
                if nb not in copied_nodes:
                    copied_nodes[nb] = Node(nb.val)
                    stack.append(nb)
                nb_copy = copied_nodes[nb]
                n_copy.neighbors.append(nb_copy)

        return root_copy
