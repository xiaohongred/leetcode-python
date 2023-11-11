from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return -1  # 一个单一节点, 其直径是0, 所以这里返回 -1,  2 + -1 + -1

            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], 2 + left + right)
            return 1 + max(left, right)

        dfs(root)
        return res[0]


if __name__ == '__main__':
    pass
