from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = {}  # map n : list of FBT

        # ret the list of fbt wiht n nodes
        def backtrack(n):
            if n == 0:
                return []
            if n == 1:
                return [TreeNode()]
            if n in dp:
                return dp[n]
            res = []
            for l in range(n):  # 左子树放l个节点，右子树放 r = n - 1 - l 个节点
                r = n - 1 - l
                leftTree = backtrack(l)  # 如果左边放l个节点无法构成fbt(正二叉树，完全二叉树)，则返回为空， 下面的for 循环也就不会执行
                rightTree = backtrack(r)
                for t1 in leftTree:
                    for t2 in rightTree:
                        res.append(TreeNode(0, t1, t2))
            dp[n] = res
            return res

        return backtrack(n)


if __name__ == '__main__':
    n = 7
    s = Solution()
    a = s.allPossibleFBT(n)
    print(a)
