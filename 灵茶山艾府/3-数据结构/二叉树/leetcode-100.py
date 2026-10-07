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
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



if __name__ == "__main__":
    s = Solution()
    # 构建两个示例二叉树
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)

    same_tree = s.isSameTree(p, q)
    print(same_tree)  # 输出两个二叉树是否相同