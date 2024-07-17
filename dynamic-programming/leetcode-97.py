class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        # rows = len(s1) +1      cols = len(s2) + 1
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]

    def isInterleaveV2(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}

        if len(s1) + len(s2) != len(s3):
            return False

        # k = i+j        s3[k]
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True

            if (i, j) in dp:
                return dp[(i, j)]
            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                dp[(i, j)] = True
                return True
            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                dp[(i, j)] = True
                return True
            dp[(i, j)] = False
            return False

        return dfs(0, 0)


if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"

    s = Solution()
    a = s.isInterleave(s1, s2, s3)
    print(a)

    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"

    a = s.isInterleave(s1, s2, s3)
    print(a)

    s1 = ""
    s2 = ""
    s3 = ""
    a = s.isInterleave(s1, s2, s3)
    print(a)
