from typing import List, Optional


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> Node:
        def construct(i: int, j: int, size: int) -> Node:
            if size == 1:
                return Node(val=grid[i][j], isLeaf=True)
            else:
                n = Node()
                sub_size = size // 2
                tl = construct(i, j, sub_size)
                tr = construct(i, j + sub_size, sub_size)
                bl = construct(i + sub_size, j, sub_size)
                br = construct(i + sub_size, j + sub_size, sub_size)
                n.val = tl.val
                if (
                    tl.isLeaf
                    and tr.isLeaf
                    and bl.isLeaf
                    and br.isLeaf
                    and len(set([tl.val, tr.val, bl.val, br.val])) == 1
                ):
                    n.isLeaf = True
                else:
                    n.isLeaf = False
                    n.topLeft = tl
                    n.topRight = tr
                    n.bottomLeft = bl
                    n.bottomRight = br

                return n

        return construct(0, 0, len(grid))
