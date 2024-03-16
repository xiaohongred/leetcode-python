from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # return pair: [withRoot, withoutRoot]
        def dfs(root):
            if not root:
                return [0, 0]

            leftPair = dfs(root.left)
            rightPair = dfs(root.right)

            withRoot = root.val + leftPair[1] + rightPair[1]
            withOutRoot = max(leftPair[0], leftPair[1]) + \
                          max(rightPair[0], rightPair[1])

            return [withRoot, withOutRoot]

        res = max(dfs(root))
        return res


if __name__ == '__main__':
    pass
