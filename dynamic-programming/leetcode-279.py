class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0
        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s ** 2
                if target - square < 0:
                    break
                dp[target] = min(dp[target], 1 + dp[target - square])
        return dp[n]


if __name__ == '__main__':
    n = 12
    s = Solution()

    a = s.numSquares(n)
    print(a)
