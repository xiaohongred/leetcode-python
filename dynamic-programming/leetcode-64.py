from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        def dfs(i, j):
            if i >= row or j >= col:
                return float("inf")

            if i == row - 1 and j == col - 1:
                return grid[i][j]
            return min(grid[i][j] + dfs(i + 1, j), grid[i][j] + dfs(i, j + 1))

        return dfs(0, 0)

    def minPathSumV2(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        cache = {}  # (i, j) -> min sum in (i,j) to grid[row-1][col-1]

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= row or j >= col:
                return float("inf")

            if i == row - 1 and j == col - 1:
                return grid[i][j]
            cache[(i, j)] = min(grid[i][j] + dfs(i + 1, j), grid[i][j] + dfs(i, j + 1))
            return cache[(i, j)]

        return dfs(0, 0)

    def minPathSumDP(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        res = [[float("inf")] * (col + 1) for r in range(row + 1)]

        res[row - 1][col] = 0
        # or res[row][col-1] = 0   只要求grid[row-1][col-1] 左边或者下面的 res 为0即可

        for r in range(row - 1, -1, -1):
            for c in range(col - 1, -1, -1):
                res[r][c] = grid[r][c] + min(res[r + 1][c], res[r][c + 1])

        return res[0][0]

    def minPathSumDP_V2(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        res = [[float("inf")] * (col + 1) for r in range(row + 1)]

        res[row][col - 1] = 0
        # or res[row - 1][col] = 0   只要求grid[row-1][col-1] 左边或者下面的 res 为0即可

        for r in range(row - 1, -1, -1):
            for c in range(col - 1, -1, -1):
                res[r][c] = grid[r][c] + min(res[r + 1][c], res[r][c + 1])

        return res[0][0]

    def minPathSumDP_V3(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        res = [[float("inf")] * (col + 1) for r in range(row + 1)]

        # res[row][col - 1] = 0
        # or res[row - 1][col] = 0   只要求grid[row-1][col-1] 左边或者下面的 res 为0即可
        # 不设置 res[row][col-1] 或者 res[row - 1][col] = 0 也可以， 在 最右下角特殊处理
        for r in range(row - 1, -1, -1):
            for c in range(col - 1, -1, -1):
                if r == row - 1 and c == col - 1:
                    res[r][c] = grid[r][c]
                else:
                    res[r][c] = grid[r][c] + min(res[r + 1][c], res[r][c + 1])

        return res[0][0]


if __name__ == '__main__':
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    s = Solution()
    a = s.minPathSum(grid)
    print(a)

    grid = [[1, 2, 3], [4, 5, 6]]
    a = s.minPathSum(grid)
    print(a)

    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    a = s.minPathSumV2(grid)
    print(a)

    grid = [[1, 2, 3], [4, 5, 6]]
    a = s.minPathSumV2(grid)
    print(a)

    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    a = s.minPathSumDP(grid)
    print(a)

    grid = [[1, 2, 3], [4, 5, 6]]
    a = s.minPathSumDP(grid)
    print(a)

    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    a = s.minPathSumDP_V2(grid)
    print(a)

    grid = [[1, 2, 3], [4, 5, 6]]
    a = s.minPathSumDP_V2(grid)
    print(a)

    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    a = s.minPathSumDP_V3(grid)
    print(a)

    grid = [[1, 2, 3], [4, 5, 6]]
    a = s.minPathSumDP_V3(grid)
    print(a)
