class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1: 1}  # num -> break elements max pow of num

        def dfs(num):
            if num in dp:
                return dp[num]
            res = 0 if num == n else num  # n 必须被分解，由n分解后得到的数num，可以保持为num
            for i in range(1, num):
                val = dfs(i) * dfs(num - i)
                res = max(res, val)
            dp[num] = res
            return res

        return dfs(n)

    def integerBreakDp(self, n: int) -> int:
        dp = {1: 1}
        for num in range(2, n + 1):
            dp[num] = 0 if num == n else num  # n 必须被分解，由n分解后得到的数num，可以保持为num
            for i in range(1, num):
                val = dp[i] * dp[num - i]
                dp[num] = max(dp[num], val)
        return dp[num]


if __name__ == '__main__':
    n = 2
    s = Solution()
    a = s.integerBreak(n)
    print(a)

    n = 10
    a = s.integerBreak(n)
    print(a)

    n = 2
    a = s.integerBreakDp(n)
    print(a)

    n = 10
    a = s.integerBreakDp(n)
    print(a)
