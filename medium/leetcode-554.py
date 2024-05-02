from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        rows = len(wall)
        gapHashTable = {0: 0}  # mapping pos:count of brick gaps
        for r in wall:
            total = 0
            for b in r[:-1]:
                total += b
                gapHashTable[total] = 1 + gapHashTable.get(total, 0)
        return rows - max(gapHashTable.values())


if __name__ == '__main__':
    wall = [[1, 2, 2, 1],
            [3, 1, 2],
            [1, 3, 2],
            [2, 4],
            [3, 1, 2],
            [1, 3, 1, 1]]
    s = Solution()
    a = s.leastBricks(wall)
    print(a)
