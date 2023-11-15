from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True

        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        l = self.isSubtree(root.left, subRoot)
        r = self.isSubtree(root.right, subRoot)
        return l or r

    def isSameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]):
        if not root1 and not root2:
            return True

        if root1 and root2 and root1.val == root2.val:
            l = self.isSameTree(root1.left, root2.left)
            r = self.isSameTree(root1.right, root2.right)
            return l and r

        return False


if __name__ == '__main__':
    pass
