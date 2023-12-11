from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        def posToVal(r, c) -> int:
            return r * n + c

        def valToPos(v):
            return [v // n, v % n]

        res = [[0] * n for i in range(m)]
        for r in range(m):
            for c in range(n):
                newVal = (posToVal(r, c) + k) % (m * n)
                newR, newC = valToPos(newVal)
                res[newR][newC] = grid[r][c]

        return res


if __name__ == '__main__':
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 1
    s = Solution()
    a = s.shiftGrid(grid, k)
    print(a)
