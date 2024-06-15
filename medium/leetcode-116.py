"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        cur, nxt = root, root.left if root else None
        while cur and nxt:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
            cur = cur.next
            if not cur:  # 如果不进入这个if分支，就一直在同一层串线
                cur = nxt  # 进入下一层
                nxt = cur.left
        return root

    def connectV2(self, root: Optional[Node]) -> Optional[Node]:
        q = deque()
        if root:
            q.append(root)

        while q:
            prev, cur = None, None
            size = len(q)
            for i in range(size):
                if i == 0:  # 每一层第一个节点特殊处理
                    prev = q.popleft()
                    cur = prev
                else:
                    cur = q.popleft()
                    prev.next = cur
                    prev = cur
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return root


if __name__ == '__main__':
    root = [1, 2, 3, 4, 5, 6, 7]
