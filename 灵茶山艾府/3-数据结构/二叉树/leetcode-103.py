# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []

        ans = []
        even = False
        cur = [root]
        while cur:
            nxt = []
            vals = []

            for node in cur:
                vals.append(node.val)
                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)

            cur = nxt
            ans.append(vals[::-1] if even else vals)
            even = not even
        return ans

if __name__ == "__main__":
    s = Solution()
    # 构建一个示例二叉树
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))

    zigzag_order = s.zigzagLevelOrder(root)
    print(zigzag_order)  # 输出二叉树的锯齿形层序遍历结果