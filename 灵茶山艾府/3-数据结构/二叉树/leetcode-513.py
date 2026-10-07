from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode | None) -> int:
        q = deque([root])
        while q:
            node = q.popleft()
            if node.right: q.append(node.right)
            if node.left: q.append(node.left)
        return node.val

if __name__ == "__main__":
    s = Solution()
    # 构建一个示例二叉树
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3, None, TreeNode(6))

    bottom_left_value = s.findBottomLeftValue(root)
    print(bottom_left_value)  # 输出二叉树的最底层最左边的值
        