from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        # dynamic programming: bottom up
        # recursive: top down

        rows = m
        cols = n
        cache = {}  # map each (r,c ) -> max length of square

        def helper(r, c):
            if r >= rows or c >= cols:
                return 0
            if (r, c) not in cache:
                down = helper(r + 1, c)
                right = helper(r, c + 1)
                diag = helper(r + 1, c + 1)
                cache[(r, c)] = 0
                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(down, right, diag)

            return cache[(r, c)]

        helper(0, 0)
        return max(cache.values()) ** 2

    def maximalSquareV2(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        cache = [[0 for _ in range(n)] for _ in range(m)]
        for r in range(m):
            if matrix[r][n - 1] == "1":
                cache[r][n - 1] = 1

        for c in range(n):
            if matrix[m - 1][c] == "1":
                cache[m - 1][c] = 1

        for r in range(m - 2, -1, -1):
            for c in range(n - 2, -1, -1):
                down = cache[r + 1][c]
                right = cache[r][c + 1]
                diag = cache[r + 1][c + 1]

                if matrix[r][c] == "1":
                    # cache[r][c] 代表以 matrix[r][c] 为左上顶点的矩阵，能够组成全“1” 的最大长度
                    cache[r][c] = 1 + min(down, right, diag)
        maxLen = 0
        for r in range(m):
            for c in range(n):
                maxLen = max(maxLen, cache[r][c])

        return maxLen ** 2


if __name__ == '__main__':
    matrix = [["1", "0", "1", "0", "0"],
              ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    s = Solution()
    a = s.maximalSquare(matrix)
    print(a)

    a = s.maximalSquareV2(matrix)
    print(a)
