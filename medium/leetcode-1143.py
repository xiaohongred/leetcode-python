import numpy as np


class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        mat = [[-1 for _ in range(n)] for _ in range(m)]

        def dp(s1: str, i: int, s2: str, j: int) -> int:
            if i == len(s1) or j == len(s2):
                return 0
            if mat[i][j] != -1:
                return mat[i][j]

            if text1[i] == text2[j]:
                mat[i][j] = 1 + dp(s1, i + 1, s2, j + 1)
            else:
                mat[i][j] = max(dp(s1, i + 1, s2, j), dp(s1, i, s2, j + 1))

            return mat[i][j]

        return dp(text1, 0, text2, 0)

    def longestCommonSubsequenceV2(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]


if __name__ == '__main__':
    s = Solution()
    text1 = "abcde"
    text2 = "ace"

    a = s.longestCommonSubsequence(text1, text2)
    print(a)
    a = s.longestCommonSubsequenceV2(text1, text2)
    print(a)
