from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        cache = {}  # map each (r, c) -> maxLength of square

        # dynamic programming: bottom up
        # recursive: top down

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
        rows = len(matrix)
        cols = len(matrix[0])

        cache = [[0 for _ in range(cols)] for _ in range(rows)]
        # dynamic programming: bottom up

        # last line
        for r in range(rows):
            if matrix[r][cols - 1] == "1":
                cache[r][cols - 1] = 1
        # last colm
        for c in range(cols):
            if matrix[rows - 1][c] == "1":
                cache[rows - 1][c] = 1

        for r in range(rows - 2, -1, -1):
            for c in range(cols - 2, -1, -1):
                down = cache[r + 1][c]
                right = cache[r][c + 1]
                diag = cache[r + 1][c + 1]
                if matrix[r][c] == "1":
                    cache[r][c] = 1 + min(down, right, diag)

        maxLen = 0
        for r in range(rows):
            for c in range(cols):
                maxLen = max(maxLen, cache[r][c])
        return maxLen ** 2


if __name__ == '__main__':
    s = Solution()
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    a = s.maximalSquareV2(matrix)
    print(a)
