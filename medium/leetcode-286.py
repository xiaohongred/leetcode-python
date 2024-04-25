# https://www.lintcode.com/problem/663/
from collections import deque
from typing import (
    List,
)


class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here
        rows, cols = len(rooms), len(rooms[0])

        visited = set()
        q = deque()  # 广度优先遍历，用队列
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:  # 门
                    q.append([r, c])
                    visited.add((r, c))

        def addRoom(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols \
                    or (r, c) in visited or rooms[r][c] == -1:  # 超范围，已经处理过，墙壁或障碍物
                return
            visited.add((r, c))  # 空房间
            q.append([r, c])

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            dist += 1


if __name__ == '__main__':
    rooms = [[2147483647, -1, 0, 2147483647],
             [2147483647, 2147483647, 2147483647, -1],
             [2147483647, -1, 2147483647, -1],
             [0, -1, 2147483647, 2147483647]]

    s = Solution()
    myInf = 2147483647
    s.walls_and_gates(rooms)
    print(rooms)
