# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []

        def preOrder(root: Optional[TreeNode]):
            if not root:
                return

            res.append("(")
            res.append(str(root.val))
            if not root.left and root.right:
                res.append("()")
            preOrder(root.left)
            preOrder(root.right)
            res.append(")")

        preOrder(root)
        return "".join(res)[1:-1]


if __name__ == '__main__':
    pass
