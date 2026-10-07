# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    prev = -float('inf')
    def isValidBST(self, root: TreeNode | None, left=-float('inf'), right=float('inf')) -> bool:
        if root is None:
            return True
        x = root.val
        return left < x < right and self.isValidBST(root.left, left, x) and self.isValidBST(root.right, x, right)
    
    def isValidBSTV2(self, root: TreeNode | None) -> bool:  # 中序遍历
        if root is None:
            return True
        if not self.isValidBSTV2(root.left):
            return False
        if root.val <= self.prev:
            return False
        self.prev = root.val
        return self.isValidBSTV2(root.right)

    def isValidBSTV3(self, root: TreeNode | None) -> bool:
        def f(node):
            if node is None:
                return float('inf'), -float('inf')
            left_min, left_max = f(node.left)
            right_min, right_max = f(node.right)
            if node.val <= left_max or node.val >= right_min:
                return float('-inf'), float('inf')
            return min(left_min, node.val), max(right_max, node.val)
        return f(root) != (float('-inf'), float('inf'))
if __name__ == "__main__":
    s = Solution()
    # 构建一个示例二叉树
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    valid_bst = s.isValidBST(root)
    print(valid_bst)  # 输出二叉树是否为有效的二叉搜索树