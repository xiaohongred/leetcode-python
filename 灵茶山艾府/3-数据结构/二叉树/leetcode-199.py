from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i == size - 1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res

    def rightSideViewV2(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def f(node, depth):
            if node is None:
                return
            if depth == len(ans):
                ans.append(node.val)
            f(node.right, depth + 1)
            f(node.left, depth + 1)
        
        f(root, 0)
        return ans

if __name__ == "__main__":
    s = Solution()
    # 构建一个示例二叉树
    root = TreeNode(1)
    root.left = TreeNode(2, None, TreeNode(5))
    root.right = TreeNode(3, None, TreeNode(4))

    right_view = s.rightSideView(root)
    print(right_view)  # 输出二叉树的右视图