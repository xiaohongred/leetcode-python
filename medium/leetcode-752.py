from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                s = lock[:i] + digit + lock[i + 1:]
                res.append(s)

                digit = str((int(lock[i]) - 1 + 10) % 10)
                s = lock[:i] + digit + lock[i + 1:]
                res.append(s)
            return res

        q = deque()
        q.append(["0000", 0])  # [lockStatus, turns]
        visited = set(deadends)  # 不能进入 deadends 状态
        while q:
            lock, turns = q.popleft()
            if lock == target:  # 如果达到目标状态，返回
                return turns
            for child in children(lock):
                if child not in visited:
                    visited.add(child)
                    q.append([child, turns + 1])

        return -1


if __name__ == '__main__':
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"
    s = Solution()
    a = s.openLock(deadends, target)
    print(a)
