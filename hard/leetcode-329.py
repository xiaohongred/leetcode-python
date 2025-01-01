from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}  # (r, c) -> LIP

        def dfs(r, c, prev):  # return LIP for (r,c)
            if (r < 0 or r >= ROWS or
                    c < 0 or c >= COLS or
                    matrix[r][c] <= prev):
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            dp[(r, c)] = res
            return res

        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                res = max(res, dfs(i, j, float('-inf')))
        return res


if __name__ == '__main__':
    s = Solution()

    matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    a = s.longestIncreasingPath(matrix)
    print(a)

    matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
    a = s.longestIncreasingPath(matrix)
    print(a)

    matrix = [[1]]
    a = s.longestIncreasingPath(matrix)
    print(a)
