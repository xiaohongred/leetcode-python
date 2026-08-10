# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def preOrder(root: Optional[TreeNode]):
            if root is None:
                return

            res.append(root.val)
            preOrder(root.left)
            preOrder(root.right)

        preOrder(root)
        return res


if __name__ == '__main__':
    pass
