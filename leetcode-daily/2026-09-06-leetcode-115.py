class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        def solve(s, t, i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0

            if s[i] == t[j]:
                return solve(s, t, i + 1, j + 1) + solve(s, t, i + 1, j)
            else:
                return solve(s, t, i + 1, j)
        return solve(s, t, 0, 0)

    def numDistinctV2(self, s: str, t: str) -> int:
        cache = {}

        def dfs(i, j):
            # dfs(i, j) 表示从 s[i:] 中组成 t[j:] 的子序列数量。
            if j == len(t):
                # t 已经匹配完成，找到一种有效方案。
                return 1
            if i == len(s):
                # s 已耗尽但 t 尚未完成，无法组成有效方案。
                return 0
            if (i, j) in cache:
                return cache[(i, j)]

            # 跳过 s[i]，继续从后面的字符中匹配 t[j:]。
            result = dfs(i + 1, j)
            if s[i] == t[j]:
                # 当前字符匹配时，也可以选择使用 s[i] 匹配 t[j]。
                result += dfs(i + 1, j + 1)

            # 缓存当前状态，避免重复计算。
            cache[(i, j)] = result
            return result

        return dfs(0, 0)
    
    def numDistinctV3(self, s: str, t: str) -> int:
        if s == "" and t == "":
            return 1
        if s == "" and t != "":
            return 0
        cache = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]

            if s[i] == t[j]:
                cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                cache[(i, j)] = dfs(i + 1, j)

            return cache[(i, j)]

        return dfs(0, 0)

    def numDistinctV4(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        cache = {}
        def solve(s, t, m, n):
            if n == 0:
                return 1
            if m == 0:
                return 0
            if (m, n) in cache:
                return cache[(m, n)]

            if s[m - 1] == t[n - 1]:
                cache[(m, n)] = solve(s, t, m - 1, n - 1) + solve(s, t, m - 1, n)
            else:
                cache[(m, n)] = solve(s, t, m - 1, n)

            return cache[(m, n)]

        return solve(s, t, m, n)
        
    def numDistinctDp(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        # dp[i][j] 表示 s 的前 i 个字符中，组成 t 的前 j 个字符的子序列数量。
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 空字符串是任意字符串的一个子序列。
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    # 当前字符可以匹配，也可以跳过。
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    # 当前字符无法匹配，只能跳过 s[i - 1]。
                    dp[i][j] = dp[i - 1][j]

        # 返回 s 的全部字符组成 t 的子序列数量。
        return dp[m][n]
    def numDistinctDpSaveSpace(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        # dp[j] 表示 s 的前 i 个字符中，组成 t 的前 j 个字符的子序列数量。
        dp = [0] * (n + 1)
        dp[0] = 1  # 空字符串是任意字符串的一个子序列。

        for i in range(1, m + 1):
            # 从后向前更新 dp 数组，避免覆盖之前的状态。
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]

    def numDistinctDpSaveSpaceV2(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        curr = [0] * (n + 1)
        prev = [0] * (n + 1)
        prev[0] = 1  # 空字符串是任意字符串的一个子
        curr[0] = 1  # 空字符串是任意字符串的一个子序列。
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    curr[j] = prev[j - 1] + prev[j]
                else:
                    curr[j] = prev[j]
            prev, curr = curr, prev  # 更新 prev 为当前行，curr 为下一行。
        return prev[n]


if __name__ == "__main__":
    s = "rabbbit"
    t = "rabbit"
    solution = Solution()
    result = solution.numDistinct(s, t)
    print(result)  # Output: 3


    s = "babgbag"
    t = "bag"
    result = solution.numDistinct(s, t)
    print(result)  # Output: 5



    s = "rabbbit"
    t = "rabbit"
    solution = Solution()
    result = solution.numDistinctV2(s, t)
    print(result)  # Output: 3


    s = "babgbag"
    t = "bag"
    result = solution.numDistinctV2(s, t)
    print(result)  # Output: 5


    s = "rabbbit"
    t = "rabbit"
    solution = Solution()
    result = solution.numDistinctDp(s, t)
    print(result)  # Output: 3


    s = "babgbag"
    t = "bag"
    result = solution.numDistinctDp(s, t)
    print(result)  # Output: 5