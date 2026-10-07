# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def get_height(node):
            if node is None:
                return 0
            
            left_height = get_height(node.left)
            if left_height == -1:
                return -1
            
            right_hegith = get_height(node.right)
            if right_hegith == -1:
                return -1
            if abs(left_height - right_hegith) > 1:
                return -1
            
            return max(left_height, right_hegith) + 1
        
        return get_height(root) != -1

if __name__ == "__main__":
    s = Solution()
    # 构建一个示例二叉树
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(3), TreeNode(4))
    root.right = TreeNode(2, None, TreeNode(3))

    balanced = s.isBalanced(root)
    print(balanced)  # 输出二叉树是否平衡

            
        