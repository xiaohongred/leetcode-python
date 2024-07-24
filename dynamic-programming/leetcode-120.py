from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cache = {}
        rowsLen = len(triangle)

        def dfs(r, c):
            if r >= rowsLen:
                return 0
            if (r, c) in cache:
                return cache[(r, c)]

            res = triangle[r][c] + min(dfs(r + 1, c), dfs(r + 1, c + 1))
            cache[(r, c)] = res
            return res

        return dfs(0, 0)

    def minimumTotalDP(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle) + 1)
        for row in triangle[::-1]:
            for i, n in enumerate(row):
                dp[i] = n + min(dp[i], dp[i + 1])
        return dp[0]


if __name__ == '__main__':
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    s = Solution()
    a = s.minimumTotal(triangle)
    print(a)

    a = s.minimumTotalDP(triangle)
    print(a)
