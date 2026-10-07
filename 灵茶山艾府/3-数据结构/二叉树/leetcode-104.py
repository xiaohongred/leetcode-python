# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        leftDep = self.maxDepth(root.left)
        rightDep = self.maxDepth(root.right)

        return max(leftDep, rightDep) + 1


if __name__ == "__main__":
    s = Solution()
    # 构建一个示例二叉树
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))

    depth = s.maxDepth(root)
    print(depth)  # 输出二叉树的最大深度