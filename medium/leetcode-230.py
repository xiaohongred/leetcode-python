# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0

        stack = []
        cur = root

        while cur or stack:  # in video, author use `and` , is a mistake ,
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val

            cur = cur.right
        return


if __name__ == '__main__':
    pass
