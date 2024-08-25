from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = {}  # (r, c) -> LIP

        def dfs(r, c, prevVal):
            if (r < 0 or r == m or c < 0 or c == n or matrix[r][c] <= prevVal):
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

        res = 1
        for r in range(m):
            for c in range(n):
                res = max(res, dfs(r, c, -1))  # 第一个元素的前一个元素当成-1,这样第一次调用dfs就不会马上返回
        return res


if __name__ == '__main__':
    matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    s = Solution()
    a = s.longestIncreasingPath(matrix)
    print(a)

    matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
    a = s.longestIncreasingPath(matrix)
    print(a)
