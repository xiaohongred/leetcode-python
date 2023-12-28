# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        l = []

        def traval(root: Optional[TreeNode]):
            if root is None:
                return
            traval(root.left)
            l.append(root.val)
            traval(root.right)

        traval(root)

        for i in range(len(l) - 1):
            if l[i + 1] <= l[i]:
                return False

        return True

    def isValidBSTV2(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False

            leftIsValid = valid(node.left, left, node.val)
            rightIsValid = valid(node.right, node.val, right)
            return leftIsValid and rightIsValid

        return valid(root, float("-inf"), float("inf"))


if __name__ == '__main__':
    pass
