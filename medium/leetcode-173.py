from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        cur = root
        while cur:
            self.stack.append(cur)
            cur = cur.left

    def next(self) -> int:
        res = self.stack.pop()

        cur = res.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return res.val

    def hasNext(self) -> bool:
        return self.stack != []


if __name__ == '__main__':
    root = TreeNode(1, None, None)
    obj = BSTIterator(root)
    print(obj.hasNext())
    param_1 = obj.next()
    print(param_1)
    param_2 = obj.hasNext()
    print(param_2)
