from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0
        row, cols = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for r in range(row):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])
        while q and fresh > 0:
            curqlen = len(q)
            for i in range(curqlen):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    # if in bounds and fresh, make rotten
                    if (row < 0 or row == len(grid)
                            or col < 0 or col == len(grid[0])
                            or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2  # make rotten
                    q.append([row, col])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1


if __name__ == '__main__':
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    s = Solution()
    a = s.orangesRotting(grid)
    print(a)
