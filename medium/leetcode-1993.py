from collections import deque
from typing import List


class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent

        self.locked = [None] * len(parent)
        self.child = {i: [] for i in range(len(parent))}
        for i in range(1, len(parent)):
            self.child[parent[i]].append(i)  # i 是 parent[i] 节点的孩子节点

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num]:
            return False
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] != user:
            return False
        self.locked[num] = None
        return True

    def upgrade(self, num: int, user: int) -> bool:
        i = num
        while i != -1:  # 本节点和其祖先节点，都未上锁
            if self.locked[i]:
                return False
            i = self.parent[i]

        lockedCount, q = 0, deque([num])
        while q:
            n = q.popleft()
            if self.locked[n]:  # 需要 num 节点的所有字节点中，至少有一个被锁了
                self.locked[n] = None  # 并给 num 节点的子节点解锁
                lockedCount += 1
            q.extend(self.child[n])
        if lockedCount > 0:
            self.locked[num] = user  # 给 num 节点加上user的锁
        return lockedCount > 0


if __name__ == '__main__':
    lockingTree = LockingTree([-1, 0, 0, 1, 1, 2, 2])
    a = lockingTree.lock(2, 2)
    print(a)
    a = lockingTree.lock(2, 3)
    print(a)
