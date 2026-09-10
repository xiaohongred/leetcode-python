# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
        self.cache = {} # root: (totalSum, count)
    
    def getNodeSubTree(self, root: TreeNode): # totalSum, count
        if root == None:
            return 0, 0
        if root in self.cache:
            return self.cache[root]
        leftTotal,  leftCount = self.getNodeSubTree(root.left)
        rightTotal, rightCount = self.getNodeSubTree(root.right)
        self.cache[root] = (root.val + leftTotal + rightTotal, 1 + leftCount + rightCount)
        return root.val + leftTotal + rightTotal,  1+leftCount+rightCount
        
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.ans = 0      # 每次调用重置，否则多次调用会互相累加
        self.cache = {}   # cache 按节点对象做 key，换一棵树也要清空
        if root == None:
            return self.ans
        
        def dfs(root: TreeNode):
            if root == None:
                return
            
            leftTotal, leftCount = self.getNodeSubTree(root.left)

            rightTotal, rightCount = self.getNodeSubTree(root.right)
            if (leftCount + rightCount) == 0:
                self.ans += 1
                return
            avg = (leftTotal + rightTotal + root.val) // (leftCount + rightCount + 1)
            if root.val == avg:
                self.ans += 1
            dfs(root.left)
            dfs(root.right)
            return
            
        dfs(root)
        return self.ans

    def averageOfSubtreeV2(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(root: TreeNode):
            if root == None:
                return 0, 0
            
            leftTotal, leftCount = dfs(root.left)
            rightTotal, rightCount = dfs(root.right)
            totalSum = leftTotal + rightTotal + root.val
            count = leftCount + rightCount + 1
            avg = totalSum // count
            if root.val == avg:
                self.ans += 1
            return totalSum, count
        
        dfs(root)
        return self.ans



if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    result = solution.averageOfSubtree(root)
    print(result)  # Output: 2

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    result = solution.averageOfSubtree(root)
    print(result)  # Output: 5


    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    result = solution.averageOfSubtreeV2(root)
    print(result)  # Output: 2

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    result = solution.averageOfSubtreeV2(root)
    print(result)  # Output: 5