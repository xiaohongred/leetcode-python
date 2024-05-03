# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(root: Optional[TreeNode]) -> Optional[TreeNode]:
            # flatten the root tree and return the list tail
            if not root:
                return None
            leftTail = dfs(root.left)
            rightTail = dfs(root.right)
            if root.left:
                leftTail.right = root.right
                root.right = root.left
                root.left = None
            return rightTail or leftTail or root

        dfs(root)
        return root


if __name__ == '__main__':
    pass
