# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):  # return max path sum without split
            if not root:
                return 0

            leftMax = dfs(root.left)
            leftMax = max(leftMax, 0)
            rightMax = dfs(root.right)
            rightMax = max(rightMax, 0)

            # compute max path sum with split
            res[0] = max(root.val + leftMax + rightMax, res[0])
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]


if __name__ == '__main__':
    s = Solution()
    root = [1, 2, 3]
    root = [-10, 9, 20, None, None, 15, 7]
