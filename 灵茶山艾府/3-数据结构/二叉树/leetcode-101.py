# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return q is p
        return p.val == q.val and self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)
    def isSymmetric(self, root: TreeNode | None) -> bool:
        return self.isSameTree(root.left, root.right)



if __name__ == "__main__":
    s = Solution()
    # 构建一个示例二叉树
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(3), TreeNode(4))
    root.right = TreeNode(2, TreeNode(4), TreeNode(3))

    symmetric = s.isSymmetric(root)
    print(symmetric)  # 输出二叉树是否对称